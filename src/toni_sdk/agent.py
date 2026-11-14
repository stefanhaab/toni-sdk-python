"""Der Agent: das Modell entscheidet, welche Funktionen es aufruft, bis die Aufgabe erledigt ist."""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Sequence, Set, Tuple

from ._generated import catalog
from .errors import ToniApiError, ToniError

if TYPE_CHECKING:
    from .client import Toni

SUCHEN = "toni_funktion_suchen"
AUFRUFEN = "toni_funktion_aufrufen"
DIREKT_GRENZE = 64
HEIKEL = ("loeschen", "veroeffentlichen")

GRUNDSATZ = (
    "Du bist Toni, der digitale Assistent eines Unternehmens. Du arbeitest mit den Funktionen der Plattform "
    "und antwortest in der Sprache der Person, kurz und konkret.\n"
    "Erfinde keine Daten: was du nicht aus einem Werkzeug-Ergebnis weißt, sagst du nicht. "
    "Meldet ein Werkzeug einen Fehler, sag in einem Satz, was nicht ging."
)


@dataclass
class Tool:
    """Ein eigenes Werkzeug, das der Agent neben den Funktionen der Plattform aufrufen darf."""

    name: str
    description: str
    execute: Callable[[Dict[str, Any]], Any]
    parameters: Dict[str, Any] = field(default_factory=lambda: {"type": "object", "properties": {}})


@dataclass
class PendingCall:
    """Ein heikler Aufruf, der auf die Bestätigung eines Menschen wartet."""

    area: str
    name: str
    title: str
    level: str
    args: Dict[str, Any]


@dataclass
class AgentStep:
    #: ``bereich/funktion`` oder der Name eines eigenen Werkzeugs
    tool: str
    name: str
    args: Dict[str, Any]
    result: Any
    #: True, wenn der Aufruf abgelehnt wurde oder die API einen Fehler meldete
    failed: bool
    ms: int
    area: Optional[str] = None
    level: Optional[str] = None


@dataclass
class AgentResult:
    #: Antwort des Agenten
    text: str
    steps: List[AgentStep]
    #: Das ganze Gespräch — für die nächste Runde an ``run(…, messages=…)`` geben.
    messages: List[Dict[str, Any]]
    usage: Dict[str, int]
    #: ``stop`` = fertig, ``max_steps`` = Rundengrenze erreicht
    finish: str


def _ohne_bestaetigung(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Entfernt die Bestätigung aus dem Schema: sie kommt nie vom Modell."""
    eigenschaften = {k: v for k, v in (schema.get("properties") or {}).items() if k != "bestaetigt"}
    pflicht = [r for r in (schema.get("required") or []) if r != "bestaetigt"]
    aus: Dict[str, Any] = {"type": "object", "properties": eigenschaften}
    if pflicht:
        aus["required"] = pflicht
    return aus


def _suche(frage: str, erlaubt: Set[str], bereich: Optional[str] = None) -> List[Tuple[dict, dict]]:
    worte = [w for w in re.split(r"[^a-z0-9äöüß]+", frage.lower()) if len(w) > 1]
    treffer: List[Tuple[int, dict, dict]] = []
    for area in catalog():
        if bereich and area["name"] != bereich:
            continue
        for fn in area["functions"]:
            if fn["level"] not in erlaubt:
                continue
            name = fn["name"].lower()
            text = f'{fn["title"]} {area["title"]} {area["name"]}'.lower()
            punkte = sum((3 if w in name else 0) + (2 if w in text else 0) for w in worte)
            if punkte > 0 or (bereich and not worte):
                treffer.append((punkte, area, fn))
    treffer.sort(key=lambda t: -t[0])
    return [(a, f) for _, a, f in treffer[:10]]


class Toolbox:
    """Die Werkzeuge eines Agenten und ihre Ausführung."""

    def __init__(
        self,
        toni: "Toni",
        *,
        areas: Optional[Sequence[str]] = None,
        allow: Optional[Sequence[str]] = None,
        on_confirm: Optional[Callable[[PendingCall], bool]] = None,
        tools: Optional[Sequence[Tool]] = None,
    ) -> None:
        self._toni = toni
        self.allow: Set[str] = set(allow or ["lesen"])
        self._on_confirm = on_confirm
        self._eigene: Dict[str, Tool] = {}
        self._direkt: Dict[str, Tuple[dict, dict]] = {}
        #: Werkzeuge im Format der Chat-API
        self.definitions: List[Dict[str, Any]] = []
        for t in tools or []:
            if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", t.name):
                raise ToniError(f"Der Werkzeugname „{t.name}“ ist ungültig (Buchstaben, Ziffern, _ und -, höchstens 64).")
            self._eigene[t.name] = t
            self._add(t.name, t.description, t.parameters)
        alle = catalog()
        self._entdecken = not areas
        if self._entdecken:
            bereiche = ", ".join(f'{a["name"]} ({a["title"]})' for a in alle)
            self._add(
                SUCHEN,
                f"Sucht Funktionen der Plattform. Bereiche: {bereiche}. Liefert Name, Titel und Parameter der passenden Funktionen.",
                {
                    "type": "object",
                    "properties": {
                        "suche": {"type": "string", "description": "Stichworte, z. B. „leads“ oder „buch kapitel“."},
                        "bereich": {"type": "string", "description": "Optional: nur in diesem Bereich suchen.", "enum": [a["name"] for a in alle]},
                    },
                    "required": ["suche"],
                },
            )
            self._add(
                AUFRUFEN,
                f"Ruft eine Funktion der Plattform auf. Bereich, Name und Parameter kommen aus {SUCHEN}.",
                {
                    "type": "object",
                    "properties": {
                        "bereich": {"type": "string"},
                        "funktion": {"type": "string"},
                        "parameter": {"type": "object", "description": "Parameter der Funktion."},
                    },
                    "required": ["bereich", "funktion"],
                },
            )
        else:
            for name in areas or []:
                area = next((a for a in alle if a["name"] == name), None)
                if area is None:
                    raise ToniError(f'Den Bereich „{name}“ gibt es nicht. Bereiche: {", ".join(a["name"] for a in alle)}.')
                for fn in area["functions"]:
                    if fn["level"] not in self.allow:
                        continue
                    tool = f'{area["name"]}__{fn["name"]}'
                    self._direkt[tool] = (area, fn)
                    self._add(tool, f'{fn["title"]} ({area["title"]})', _ohne_bestaetigung(fn["parameters"]))
            if len(self._direkt) > DIREKT_GRENZE:
                raise ToniError(
                    f"{len(self._direkt)} Funktionen sind zu viele für ein Gespräch (höchstens {DIREKT_GRENZE}). "
                    "Wähle weniger Bereiche oder lass `areas` weg, dann sucht der Agent selbst."
                )

    def _add(self, name: str, description: str, parameters: Dict[str, Any]) -> None:
        self.definitions.append({"type": "function", "function": {"name": name, "description": description, "parameters": parameters}})

    @property
    def names(self) -> List[str]:
        return [d["function"]["name"] for d in self.definitions]

    def call(self, tool: str, args: Dict[str, Any]) -> Tuple[Any, Optional[AgentStep]]:
        """Führt ein Werkzeug aus. Liefert (Ergebnis, Schritt); Suchen im Katalog ist kein Schritt."""
        start = time.monotonic()

        def ms() -> int:
            return int((time.monotonic() - start) * 1000)

        eigenes = self._eigene.get(tool)
        if eigenes:
            try:
                step = AgentStep(tool=tool, name=tool, args=args, result=eigenes.execute(args), failed=False, ms=ms())
            except Exception as e:  # noqa: BLE001 - der Fehler geht als Ergebnis ans Modell
                step = AgentStep(tool=tool, name=tool, args=args, result={"error": str(e)}, failed=True, ms=ms())
            return step.result, step

        if self._entdecken and tool == SUCHEN:
            bereich = args.get("bereich") if isinstance(args.get("bereich"), str) else None
            treffer = _suche(str(args.get("suche") or ""), self.allow, bereich)
            if not treffer:
                return {"hinweis": "Keine passende Funktion gefunden, die dieser Agent nutzen darf. Versuch andere Stichworte oder einen Bereich."}, None
            return [
                {"bereich": a["name"], "funktion": f["name"], "titel": f["title"], "stufe": f["level"], "parameter": _ohne_bestaetigung(f["parameters"])}
                for a, f in treffer
            ], None

        ziel: Optional[Tuple[dict, dict]] = None
        parameter: Any = args
        if self._entdecken and tool == AUFRUFEN:
            area = next((a for a in catalog() if a["name"] == args.get("bereich")), None)
            fn = next((f for f in area["functions"] if f["name"] == args.get("funktion")), None) if area else None
            if area and fn:
                ziel = (area, fn)
            parameter = args.get("parameter") if isinstance(args.get("parameter"), dict) else {}
        else:
            ziel = self._direkt.get(tool)
        if ziel is None:
            return {"error": f'Die Funktion „{args.get("bereich", "")}/{args.get("funktion", tool)}“ gibt es nicht.'}, None

        area, fn = ziel
        sauber = {k: v for k, v in parameter.items() if k != "bestaetigt"}

        def schritt(result: Any, failed: bool) -> Tuple[Any, AgentStep]:
            return result, AgentStep(
                tool=f'{area["name"]}/{fn["name"]}', area=area["name"], name=fn["name"], level=fn["level"],
                args=sauber, result=result, failed=failed, ms=ms(),
            )

        if fn["level"] not in self.allow:
            return schritt({"error": f'Dieser Agent darf keine Funktionen der Stufe „{fn["level"]}“ nutzen.'}, True)
        confirmed = False
        if fn["level"] in HEIKEL:
            if self._on_confirm is None:
                return schritt({"error": "Diese Aktion ist unumkehrbar oder wirkt nach außen und braucht die Bestätigung eines Menschen. Die ist hier nicht eingerichtet."}, True)
            confirmed = self._on_confirm(PendingCall(area=area["name"], name=fn["name"], title=fn["title"], level=fn["level"], args=sauber)) is True
            if not confirmed:
                return schritt({"error": "Die Person hat diese Aktion nicht bestätigt."}, True)
        try:
            result = self._toni.platform.call(area["name"], fn["name"], sauber, confirmed=confirmed)
        except ToniApiError as e:
            return schritt({"error": str(e), "code": e.code}, True)
        return schritt(result, isinstance(result, dict) and result.get("success") is False)


class Agent:
    """Ein Agent mit festen Einstellungen. ``run`` führt eine Aufgabe aus."""

    def __init__(
        self,
        toni: "Toni",
        *,
        model: str = "toni-mittel",
        instructions: Optional[str] = None,
        areas: Optional[Sequence[str]] = None,
        allow: Optional[Sequence[str]] = None,
        on_confirm: Optional[Callable[[PendingCall], bool]] = None,
        tools: Optional[Sequence[Tool]] = None,
        max_steps: int = 12,
        temperature: Optional[float] = None,
        on_step: Optional[Callable[[AgentStep], None]] = None,
        max_result_chars: int = 24_000,
    ) -> None:
        self._toni = toni
        self._model = model
        self._instructions = instructions
        self._max_steps = max_steps
        self._temperature = temperature
        self._on_step = on_step
        self._max_result_chars = max_result_chars
        self.toolbox = Toolbox(toni, areas=areas, allow=allow, on_confirm=on_confirm, tools=tools)

    @property
    def tool_names(self) -> List[str]:
        """Die Werkzeuge, die das Modell in diesem Agenten sieht."""
        return self.toolbox.names

    def run(self, input: str, *, messages: Optional[List[Dict[str, Any]]] = None) -> AgentResult:  # noqa: A002
        """Führt eine Aufgabe aus. ``messages`` = Gespräch des letzten Laufs, um weiterzusprechen."""
        verlauf: List[Dict[str, Any]] = (
            list(messages)
            if messages
            else [{"role": "system", "content": f"{GRUNDSATZ}\n\n{self._instructions}" if self._instructions else GRUNDSATZ}]
        )
        verlauf.append({"role": "user", "content": input})
        steps: List[AgentStep] = []
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}

        runde = 0
        while True:
            letzte = runde >= self._max_steps
            params: Dict[str, Any] = {"model": self._model, "messages": verlauf}
            if self.toolbox.definitions and not letzte:
                params["tools"] = self.toolbox.definitions
            if self._temperature is not None:
                params["temperature"] = self._temperature
            r = self._toni.chat.completions.create(**params)
            for k in usage:
                usage[k] += int((r.get("usage") or {}).get(k) or 0)
            choices = r.get("choices") or []
            m = choices[0].get("message") if choices else None
            if not m:
                raise ToniError("Die Toni API hat keine Antwort geliefert.")
            calls = [] if letzte else (m.get("tool_calls") or [])
            eintrag: Dict[str, Any] = {"role": "assistant", "content": m.get("content")}
            if calls:
                eintrag["tool_calls"] = calls
            verlauf.append(eintrag)
            if not calls:
                return AgentResult(text=m.get("content") or "", steps=steps, messages=verlauf, usage=usage, finish="max_steps" if letzte else "stop")

            for call in calls:
                fn = call.get("function") or {}
                try:
                    args = json.loads(fn.get("arguments") or "{}")
                    if not isinstance(args, dict):
                        raise ValueError
                except ValueError:
                    ergebnis: Any = {"error": "Die Parameter waren kein gültiges JSON."}
                else:
                    ergebnis, step = self.toolbox.call(str(fn.get("name") or ""), args)
                    if step:
                        steps.append(step)
                        if self._on_step:
                            self._on_step(step)
                text = ergebnis if isinstance(ergebnis, str) else json.dumps(ergebnis, ensure_ascii=False, default=str)
                if len(text) > self._max_result_chars:
                    text = text[: self._max_result_chars] + f"\n… (gekürzt, {len(text)} Zeichen insgesamt. Grenze die Abfrage ein, z. B. mit limit.)"
                verlauf.append({"role": "tool", "tool_call_id": call.get("id"), "content": text})
            runde += 1

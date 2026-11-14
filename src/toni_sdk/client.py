"""Client für die Toni API (https://ki-markt.com)."""
from __future__ import annotations

import os
import re
import time
from typing import Any, Callable, Dict, Iterator, List, Mapping, Optional, Sequence, Tuple, Union
from urllib.parse import quote

from ._generated import catalog
from ._generated.areas import AREAS, AreaAccess
from ._http import Http, multipart, sse
from .agent import Agent, AgentStep, PendingCall, Tool
from .errors import ToniError

FileInput = Union[str, "os.PathLike[str]", bytes, Tuple[str, bytes]]


class _Completions:
    def __init__(self, http: Http) -> None:
        self._http = http

    def create(self, *, model: str, messages: List[Dict[str, Any]], stream: bool = False, timeout: Optional[float] = None, **weitere: Any) -> Any:
        """Chat, OpenAI-kompatibel. Mit ``stream=True`` kommt ein Iterator von Stücken."""
        body = {"model": model, "messages": messages, **weitere}
        if stream:
            body["stream"] = True
            antwort = self._http.request("/chat/completions", body=body, raw=True, timeout=timeout, headers={"Accept": "text/event-stream"})
            return sse(antwort)
        return self._http.request("/chat/completions", body=body, timeout=timeout)


class _Chat:
    def __init__(self, http: Http) -> None:
        self.completions = _Completions(http)


class Platform:
    """Die Funktionen der Plattform, frei aufrufbar."""

    def __init__(self, http: Http) -> None:
        self._http = http

    def call(self, area: str, name: str, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, timeout: Optional[float] = None) -> Dict[str, Any]:
        """Ruft eine Funktion auf und liefert ihre Rückgabe (``data`` der Hülle)."""
        return self.raw(area, name, params, confirmed=confirmed, timeout=timeout)["data"]

    def raw(self, area: str, name: str, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, timeout: Optional[float] = None) -> Dict[str, Any]:
        """Wie ``call``, liefert aber die ganze Hülle (``bereich``, ``werkzeug``, ``stufe``, ``data``)."""
        if not re.fullmatch(r"[a-z_]+", area) or not re.fullmatch(r"[a-z0-9_]+", name):
            raise ToniError(f"Unbekannte Funktion „{area}/{name}“.")
        body = dict(params or {})
        if confirmed:
            body["bestaetigt"] = True
        # Schreibende Aufrufe werden nicht von selbst wiederholt: ein zweiter Versuch könnte doppelt anlegen.
        return self._http.request(f"/platform/{area}/{name}", method="POST", body=body, no_retry=True, timeout=timeout)

    def catalog(self) -> Dict[str, Any]:
        """Bereiche und Funktionen samt der Rechte DIESES Schlüssels (``erlaubt``)."""
        return self._http.request("/platform")

    def concepts(self) -> Dict[str, Any]:
        """Kapitel „Toni und der Kontext deines Unternehmens“ (öffentlich)."""
        return self._http.request("/platform/konzepte", anonymous=True)

    def openapi(self) -> Dict[str, Any]:
        """OpenAPI-Dokument der ganzen API (öffentlich)."""
        return self._http.request("/platform/openapi.json", anonymous=True)

    @property
    def functions(self) -> List[Dict[str, Any]]:
        """Der Katalog, mit dem dieses Paket erzeugt wurde (ohne Netzwerk)."""
        return catalog()


class _Embeddings:
    def __init__(self, http: Http) -> None:
        self._http = http

    def create(self, *, input: Union[str, Sequence[str]], model: str = "toni-embedding") -> Dict[str, Any]:  # noqa: A002
        return self._http.request("/embeddings", body={"model": model, "input": input})


def _als_datei(file: FileInput) -> Tuple[str, bytes]:
    if isinstance(file, tuple):
        return file[0], bytes(file[1])
    if isinstance(file, (bytes, bytearray)):
        return "audio", bytes(file)
    pfad = os.fspath(file)
    with open(pfad, "rb") as f:
        return os.path.basename(pfad), f.read()


class _Transcriptions:
    def __init__(self, http: Http) -> None:
        self._http = http

    def create(self, *, file: FileInput, model: str = "toni-transkription", language: Optional[str] = None, response_format: Optional[str] = None) -> Dict[str, Any]:
        """``file``: Dateipfad, Bytes oder ``(Dateiname, Bytes)``. Höchstens 25 MB."""
        name, inhalt = _als_datei(file)
        felder = {"model": model}
        if language:
            felder["language"] = language
        if response_format:
            felder["response_format"] = response_format
        r = self._http.request("/audio/transcriptions", method="POST", form=multipart(felder, ("file", name, inhalt)))
        return {"text": r} if isinstance(r, str) else r


class _Audio:
    def __init__(self, http: Http) -> None:
        self.transcriptions = _Transcriptions(http)


class _Images:
    def __init__(self, http: Http) -> None:
        self._http = http

    def generate(self, *, prompt: str, model: str = "toni-bild", **weitere: Any) -> Dict[str, Any]:
        return self._http.request("/images/generations", body={"model": model, "prompt": prompt, **weitere}, no_retry=True)


class _Videos:
    def __init__(self, http: Http) -> None:
        self._http = http

    def create(self, *, prompt: str, model: str = "toni-video", **weitere: Any) -> Dict[str, Any]:
        return self._http.request("/videos", body={"model": model, "prompt": prompt, **weitere}, no_retry=True)

    def retrieve(self, id: str) -> Dict[str, Any]:  # noqa: A002
        return self._http.request(f"/videos/{quote(id, safe='')}")

    def content(self, id: str) -> bytes:  # noqa: A002
        """Die fertige MP4-Datei."""
        with self._http.request(f"/videos/{quote(id, safe='')}/content", raw=True, headers={"Accept": "video/mp4"}) as antwort:
            return antwort.read()

    def wait(self, id: str, *, interval: float = 5.0, timeout: float = 600.0) -> Dict[str, Any]:  # noqa: A002
        """Fragt ab, bis das Video fertig oder gescheitert ist."""
        ende = time.monotonic() + timeout
        while True:
            v = self.retrieve(id)
            if v.get("status") in ("completed", "failed"):
                return v
            if time.monotonic() > ende:
                raise ToniError(f"Das Video {id} ist nach der Wartezeit noch nicht fertig.")
            time.sleep(interval)


class _Models:
    def __init__(self, http: Http) -> None:
        self._http = http

    def list(self) -> Dict[str, Any]:
        return self._http.request("/models")


class Toni(AreaAccess):
    """Client für die Toni API.

    >>> toni = Toni()                                   # liest TONI_API_KEY
    >>> toni.ask("Was ist ein Voicebot?")
    >>> toni.crm.get_leads(status="new")
    >>> toni.agent(areas=["crm"]).run("Wer hat sich diese Woche gemeldet?").text
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        timeout: float = 120.0,
        max_retries: int = 2,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        self._http = Http(api_key, base_url, timeout, max_retries, headers)
        self.chat = _Chat(self._http)
        self.platform = Platform(self._http)
        self.embeddings = _Embeddings(self._http)
        self.audio = _Audio(self._http)
        self.images = _Images(self._http)
        self.videos = _Videos(self._http)
        self.models = _Models(self._http)
        self._bereiche: Dict[str, Any] = {}

    def _area(self, name: str) -> Any:
        if name not in self._bereiche:
            self._bereiche[name] = AREAS[name](self.platform)
        return self._bereiche[name]

    @property
    def base_url(self) -> str:
        """Die Adresse, gegen die der Client arbeitet."""
        return self._http.base_url

    def prices(self) -> Dict[str, Any]:
        """Größen und Preise (öffentlich, ohne Schlüssel)."""
        return self._http.request("/preise", anonymous=True)

    def ask(self, prompt: str, *, model: str = "toni-mittel", system: Optional[str] = None, temperature: Optional[float] = None, max_tokens: Optional[int] = None) -> str:
        """Eine Frage, eine Antwort als Text."""
        messages: List[Dict[str, Any]] = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        extra: Dict[str, Any] = {}
        if temperature is not None:
            extra["temperature"] = temperature
        if max_tokens is not None:
            extra["max_tokens"] = max_tokens
        r = self.chat.completions.create(model=model, messages=messages, **extra)
        choices = r.get("choices") or []
        return (choices[0].get("message", {}).get("content") or "") if choices else ""

    def stream(self, prompt: str, *, model: str = "toni-mittel", system: Optional[str] = None) -> Iterator[str]:
        """Wie ``ask``, liefert die Antwort aber Stück für Stück."""
        messages: List[Dict[str, Any]] = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
        for stueck in self.chat.completions.create(model=model, messages=messages, stream=True):
            for c in stueck.get("choices") or []:
                text = (c.get("delta") or {}).get("content")
                if text:
                    yield text

    def agent(
        self,
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
    ) -> Agent:
        """Ein Agent: das Modell entscheidet, welche Funktionen der Plattform (und welche eigenen Werkzeuge)
        es aufruft, bis die Aufgabe erledigt ist. Standard: nur lesende Funktionen.

        ``allow``: Stufen, die er nutzen darf (``lesen``, ``schreiben``, ``veroeffentlichen``, ``loeschen``).
        ``loeschen`` und ``veroeffentlichen`` laufen zusätzlich nur mit ``on_confirm``; das Modell kann
        die Bestätigung nicht selbst setzen.
        """
        return Agent(
            self, model=model, instructions=instructions, areas=areas, allow=allow, on_confirm=on_confirm, tools=tools,
            max_steps=max_steps, temperature=temperature, on_step=on_step, max_result_chars=max_result_chars,
        )

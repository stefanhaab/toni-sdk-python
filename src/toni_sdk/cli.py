"""``toni`` im Terminal."""
from __future__ import annotations

import json
import sys
from typing import List, Optional

from . import Toni, ToniError, VERSION, catalog

HILFE = f"""toni {VERSION} — Toni im Terminal (https://ki-markt.com)

  toni "Wer hat sich diese Woche gemeldet?"     eine Aufgabe, eine Antwort
  toni                                           Gespräch (beenden mit Strg+D)
  toni funktionen [suche]                        Funktionen der Plattform auflisten
  toni preise                                    Größen und Preise

Optionen:
  --bereiche crm,offers   nur diese Bereiche (sonst sucht Toni selbst im Katalog)
  --modell toni-schwer    Größe: toni-leicht, toni-mittel (Standard), toni-schwer
  --schreiben             Toni darf auch anlegen und ändern (Standard: nur lesen)
  --alles                 zusätzlich löschen und veröffentlichen, jeweils mit Rückfrage
  --leise                 Werkzeugaufrufe nicht anzeigen

Schlüssel: Umgebungsvariable TONI_API_KEY (km_live_…), aus dem Konto unter „API“."""


def _lauf(args: List[str]) -> None:
    def schalter(n: str) -> bool:
        if n in args:
            args.remove(n)
            return True
        return False

    def wert(n: str) -> Optional[str]:
        if n not in args:
            return None
        i = args.index(n)
        w = args[i + 1] if i + 1 < len(args) else None
        del args[i : i + 2]
        return w

    if schalter("--help") or schalter("-h"):
        return print(HILFE)
    if schalter("--version") or schalter("-v"):
        return print(VERSION)
    roh = wert("--bereiche")
    bereiche = [s.strip() for s in roh.split(",") if s.strip()] if roh else None
    modell = wert("--modell") or "toni-mittel"
    alles = schalter("--alles")
    schreiben = schalter("--schreiben") or alles
    leise = schalter("--leise")

    if args[:1] == ["funktionen"]:
        frage = " ".join(args[1:]).lower()
        for a in catalog():
            treffer = [f for f in a["functions"] if not frage or frage in f'{a["name"]} {a["title"]} {f["name"]} {f["title"]}'.lower()]
            if not treffer:
                continue
            print(f'\n{a["title"]} ({a["name"]})')
            for f in treffer:
                print(f'  {f["name"]:<38} {f["level"]:<17} {f["title"]}')
        return None

    toni = Toni()
    if args[:1] == ["preise"]:
        for m in toni.prices().get("data", []):
            print(f'{m.get("id", ""):<22} {str(m.get("name", "")):<16} {json.dumps(m.get("preis"), ensure_ascii=False)}')
        return None
    tty = sys.stdin.isatty()
    allow = ["lesen", "schreiben", "veroeffentlichen", "loeschen"] if alles else ["lesen", "schreiben"] if schreiben else ["lesen"]

    def bestaetigen(c) -> bool:
        antwort = input(f"\n{c.title} ({c.area}/{c.name}) {json.dumps(c.args, ensure_ascii=False)}\nWirklich ausführen? [j/N] ")
        return antwort.strip().lower().startswith("j")

    def zeigen(s) -> None:
        sys.stderr.write(f'  {"✗" if s.failed else "→"} {s.tool} {json.dumps(s.args, ensure_ascii=False)} ({s.ms} ms)\n')

    agent = toni.agent(areas=bereiche, model=modell, allow=allow, on_step=None if leise else zeigen, on_confirm=bestaetigen if tty else None)

    frage = " ".join(args).strip()
    if frage:
        return print(agent.run(frage).text)
    if not tty:
        text = sys.stdin.read().strip()
        return print(agent.run(text).text if text else HILFE)

    print(f'Toni {VERSION} · {", ".join(allow)} · Strg+D beendet')
    messages = None
    while True:
        try:
            eingabe = input("\n› ").strip()
        except EOFError:
            break
        if not eingabe:
            continue
        if eingabe in ("exit", "ende"):
            break
        try:
            r = agent.run(eingabe, messages=messages)
        except ToniError as e:
            print(f"\n{e}", file=sys.stderr)
            continue
        messages = r.messages
        print(f"\n{r.text}")
    return None


def main() -> None:
    try:
        _lauf(sys.argv[1:])
    except ToniError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Erzeugt src/toni_sdk/_generated/* aus der OpenAPI-Datei der Toni API.

    python3 scripts/generate.py                 (lädt https://api.ki-markt.com/v1/platform/openapi.json)
    python3 scripts/generate.py pfad/openapi.json
"""
import json
import keyword
import os
import re
import sys
import urllib.request
from pathlib import Path

QUELLE = (sys.argv[1] if len(sys.argv) > 1 else None) or os.environ.get("TONI_OPENAPI") or "https://api.ki-markt.com/v1/platform/openapi.json"
ZIEL = Path(__file__).resolve().parent.parent / "src" / "toni_sdk" / "_generated"

if re.match(r"https?:", QUELLE):
    with urllib.request.urlopen(QUELLE, timeout=60) as r:  # noqa: S310
        doc = json.load(r)
else:
    doc = json.loads(Path(QUELLE).read_text(encoding="utf-8"))


def glatt(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


def kurz(s, n):
    t = glatt(s)
    return t[: n - 1].rstrip() + "…" if len(t) > n else t


def doku(s):
    return glatt(s).replace("\\", "\\\\").replace('"""', "'''")


def erster_satz(s):
    t = glatt(str(s or "").replace("**", ""))
    m = re.match(r"^.*?[.!?](\s|$)", t)
    return (m.group(0) if m else t).strip()


def typ(p):
    t = p.get("type") if isinstance(p, dict) else None
    if isinstance(t, list):
        t = next((x for x in t if x != "null"), None)
    return t if isinstance(t, str) else None


PY = {"string": "str", "integer": "int", "number": "float", "boolean": "bool", "array": "list", "object": "dict"}


def schlank(p):
    o = {}
    t = typ(p)
    if t:
        o["type"] = t
    if isinstance(p, dict) and p.get("description"):
        o["description"] = kurz(p["description"], 180)
    if isinstance(p, dict) and isinstance(p.get("enum"), list):
        o["enum"] = p["enum"]
    if t == "array":
        o["items"] = schlank(p["items"]) if isinstance(p.get("items"), dict) else {}
    return o


def pascal(s):
    return "".join(w[:1].upper() + w[1:] for w in s.split("_") if w)


def bezeichner(s):
    return s + "_" if keyword.iskeyword(s) else s


tag_text = {t["name"]: t.get("description", "") for t in doc.get("tags", [])}
bereiche = {}
for pfad, eintrag in doc["paths"].items():
    m = re.match(r"^/platform/([a-z_]+)/([a-z0-9_]+)$", pfad)
    if not m or "post" not in eintrag:
        continue
    bereich, name = m.groups()
    op = eintrag["post"]
    schema = (((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}).get("schema") or {}
    tag = (op.get("tags") or [bereich])[0]
    b = bereiche.setdefault(bereich, {"name": bereich, "title": tag, "description": erster_satz(tag_text.get(tag, "")), "functions": []})
    b["functions"].append({
        "name": name,
        "title": op.get("summary") or name,
        "level": op.get("x-stufe") or "lesen",
        "properties": schema.get("properties") if isinstance(schema.get("properties"), dict) else {},
        "required": schema.get("required") or [],
    })
if not bereiche:
    sys.exit("Keine Plattform-Funktionen in der OpenAPI-Datei gefunden.")

info = doc.get("info") or {}
version = str(info.get("version") or "")

# ---------------------------------------------------------------- catalog.json
katalog = []
anzahl = 0
for b in bereiche.values():
    fns = []
    for f in b["functions"]:
        params = {"type": "object", "properties": {k: schlank(v) for k, v in f["properties"].items()}}
        if f["required"]:
            params["required"] = list(f["required"])
        fns.append({"name": f["name"], "title": f["title"], "level": f["level"], "parameters": params})
        anzahl += 1
    katalog.append({"name": b["name"], "title": b["title"], "description": b["description"], "functions": fns})

ZIEL.mkdir(parents=True, exist_ok=True)
(ZIEL / "catalog.json").write_text(json.dumps({"api_version": version, "areas": katalog}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

kopf = f'# ERZEUGT von scripts/generate.py aus der OpenAPI-Datei ({info.get("title")} {version}). Nicht von Hand ändern.\n'

(ZIEL / "__init__.py").write_text(kopf + f'''"""Der Katalog, aus dem dieses Paket erzeugt wurde: {len(katalog)} Bereiche, {anzahl} Funktionen."""
import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

#: Stand der API, aus dem dieses Paket erzeugt wurde.
API_VERSION = {version!r}


@lru_cache(maxsize=1)
def catalog() -> List[Dict[str, Any]]:
    """Alle Bereiche mit ihren Funktionen (Name, Titel, Stufe, Parameter)."""
    return json.loads((Path(__file__).parent / "catalog.json").read_text(encoding="utf-8"))["areas"]
''', encoding="utf-8")

# ---------------------------------------------------------------- areas.py
out = kopf + '''"""Jede Funktion der Plattform als Methode: ``toni.<bereich>.<funktion>(…)``."""
from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Type


class _Area:
    def __init__(self, platform: Any) -> None:
        self._platform = platform
'''
felder = []
for b in bereiche.values():
    klasse = pascal(b["name"]) + "Area"
    titel = doku(b["title"]) + (" — " + doku(b["description"]) if b["description"] else "")
    out += f'\n\nclass {klasse}(_Area):\n    """{titel}"""\n'
    for f in b["functions"]:
        if "params" in f["properties"] or "confirmed" in f["properties"]:
            sys.exit(f'{b["name"]}/{f["name"]}: der Parametername kollidiert mit der Signatur.')
        heikel = f["level"] in ("loeschen", "veroeffentlichen")
        zeilen = ""
        for k, v in f["properties"].items():
            v = v if isinstance(v, dict) else {}
            art = PY.get(typ(v) or "", "Any")
            pflicht = ", Pflicht" if k in f["required"] else ""
            text = ": " + doku(kurz(v.get("description"), 220)) if v.get("description") else ""
            zeilen += f"        - ``{k}`` ({art}{pflicht}){text}\n"
        sig = "self, params: Optional[Mapping[str, Any]] = None" + (", *, confirmed: bool = False" if heikel else "") + ", **kwargs: Any"
        out += f'\n    def {bezeichner(f["name"])}({sig}) -> Dict[str, Any]:\n'
        out += f'        """{doku(f["title"])}\n\n        Recht am Schlüssel: ``{f["level"]}`` · ``POST /platform/{b["name"]}/{f["name"]}``\n'
        if zeilen:
            out += "\n        Parameter (als ``params``-Dict oder Schlüsselwort):\n\n" + zeilen
        if heikel:
            out += "\n        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).\n"
        out += '        """\n'
        out += f'        return self._platform.call("{b["name"]}", "{f["name"]}", {{**(params or {{}}), **kwargs}}' + (", confirmed=confirmed" if heikel else "") + ")\n"
    felder.append((bezeichner(b["name"]), b["name"], klasse, b["title"]))

out += "\n\n#: Bereichsname → Klasse\nAREAS: Dict[str, Type[_Area]] = {\n"
for _, name, klasse, _t in felder:
    out += f'    "{name}": {klasse},\n'
out += '}\n\n\nclass AreaAccess:\n    """Die Bereiche der Plattform als Eigenschaften des Clients."""\n\n    def _area(self, name: str) -> Any:  # vom Client überschrieben\n        raise NotImplementedError\n'
for feld, name, klasse, titel in felder:
    out += f'\n    @property\n    def {feld}(self) -> {klasse}:\n        """{doku(titel)}"""\n        return self._area("{name}")\n'
(ZIEL / "areas.py").write_text(out, encoding="utf-8")

print(f"{len(katalog)} Bereiche, {anzahl} Funktionen → src/toni_sdk/_generated/")

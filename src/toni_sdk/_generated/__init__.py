# ERZEUGT von scripts/generate.py aus der OpenAPI-Datei (KI-Markt API 1.0.0-beta). Nicht von Hand ändern.
"""Der Katalog, aus dem dieses Paket erzeugt wurde: 30 Bereiche, 265 Funktionen."""
import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

#: Stand der API, aus dem dieses Paket erzeugt wurde.
API_VERSION = '1.0.0-beta'


@lru_cache(maxsize=1)
def catalog() -> List[Dict[str, Any]]:
    """Alle Bereiche mit ihren Funktionen (Name, Titel, Stufe, Parameter)."""
    return json.loads((Path(__file__).parent / "catalog.json").read_text(encoding="utf-8"))["areas"]

"""HTTP-Schicht: nur Standardbibliothek, Wiederholungen, Ströme, Datei-Upload."""
from __future__ import annotations

import json
import os
import random
import socket
import time
import urllib.error
import urllib.request
import uuid
from typing import Any, Dict, Iterator, Mapping, Optional, Tuple

from .errors import ToniConnectionError, ToniError, api_error

VERSION = "0.1.0"
DEFAULT_BASE_URL = "https://api.ki-markt.com/v1"

_WIEDERHOLEN = {429, 502, 503, 504}
_SCHLUESSEL_FEHLT = "Der Schlüssel fehlt. Übergib `api_key`, setze die Umgebungsvariable TONI_API_KEY (km_live_…) oder nutze im Terminal `toni login`."


def _pause(versuch: int) -> float:
    return min(0.5 * 2**versuch, 8.0) + random.random() * 0.25


def multipart(felder: Mapping[str, str], datei: Tuple[str, str, bytes]) -> Tuple[bytes, str]:
    """Baut einen multipart/form-data-Körper. ``datei`` = (Feldname, Dateiname, Bytes)."""
    grenze = "toni" + uuid.uuid4().hex
    teile = []
    for name, wert in felder.items():
        teile.append(f'--{grenze}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{wert}\r\n'.encode())
    feld, dateiname, inhalt = datei
    sauber = dateiname.replace('"', "").replace("\r", "").replace("\n", "")
    teile.append(
        f'--{grenze}\r\nContent-Disposition: form-data; name="{feld}"; filename="{sauber}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n".encode() + inhalt + b"\r\n"
    )
    teile.append(f"--{grenze}--\r\n".encode())
    return b"".join(teile), f"multipart/form-data; boundary={grenze}"


class Http:
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 120.0,
        max_retries: int = 2,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        self._api_key = api_key or os.environ.get("TONI_API_KEY") or os.environ.get("KM_KEY")
        self.base_url = (base_url or os.environ.get("TONI_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self._headers = dict(headers or {})

    def key(self) -> str:
        """Der Schlüssel, oder ein klarer Fehler, wenn er fehlt."""
        if not self._api_key:
            raise ToniError(_SCHLUESSEL_FEHLT)
        return self._api_key

    def request(
        self,
        path: str,
        *,
        method: Optional[str] = None,
        body: Any = None,
        form: Optional[Tuple[bytes, str]] = None,
        anonymous: bool = False,
        raw: bool = False,
        no_retry: bool = False,
        timeout: Optional[float] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any:
        """Sendet eine Anfrage. Mit ``raw`` kommt die offene Antwort zurück (Ströme, Dateien)."""
        if not anonymous and not self._api_key:
            raise ToniError(_SCHLUESSEL_FEHLT)
        kopf: Dict[str, str] = {"Accept": "application/json", "User-Agent": f"toni-sdk-python/{VERSION}"}
        kopf.update(self._headers)
        kopf.update(headers or {})
        if not anonymous:
            kopf["Authorization"] = f"Bearer {self._api_key}"
        daten: Optional[bytes] = None
        if form is not None:
            daten, kopf["Content-Type"] = form
        elif body is not None:
            daten = json.dumps(body, ensure_ascii=False).encode("utf-8")
            kopf["Content-Type"] = "application/json"
        methode = method or ("POST" if daten is not None else "GET")
        versuche = 0 if no_retry else self.max_retries
        grenze = self.timeout if timeout is None else timeout

        versuch = 0
        while True:
            anfrage = urllib.request.Request(self.base_url + path, data=daten, headers=kopf, method=methode)
            try:
                antwort = urllib.request.urlopen(anfrage, timeout=grenze)  # noqa: S310 - Adresse kommt aus der Konfiguration
            except urllib.error.HTTPError as e:
                text = e.read().decode("utf-8", "replace")
                try:
                    inhalt: Any = json.loads(text)
                except ValueError:
                    inhalt = text
                if e.code in _WIEDERHOLEN and versuch < versuche:
                    try:
                        nach = float(e.headers.get("Retry-After") or 0)
                    except ValueError:
                        nach = 0.0
                    time.sleep(min(nach, 30.0) if nach > 0 else _pause(versuch))
                    versuch += 1
                    continue
                raise api_error(e.code, inhalt) from None
            except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as e:
                if versuch < versuche:
                    time.sleep(_pause(versuch))
                    versuch += 1
                    continue
                grund = getattr(e, "reason", e)
                zeit = isinstance(grund, (socket.timeout, TimeoutError)) or isinstance(e, (socket.timeout, TimeoutError))
                raise ToniConnectionError(
                    "Die Toni API hat nicht rechtzeitig geantwortet." if zeit else "Die Toni API ist nicht erreichbar."
                ) from e

            if raw:
                return antwort
            try:
                with antwort:
                    text = antwort.read().decode("utf-8", "replace")
                    typ = antwort.headers.get("Content-Type") or ""
                return json.loads(text) if "json" in typ else text
            except (ValueError, OSError) as e:
                raise ToniConnectionError("Die Antwort der Toni API war nicht lesbar.") from e


def sse(antwort: Any) -> Iterator[Dict[str, Any]]:
    """Liest einen Server-Sent-Events-Strom und liefert die JSON-Stücke bis ``[DONE]``."""
    try:
        zeilen: list = []
        for roh in antwort:
            zeile = roh.decode("utf-8", "replace").rstrip("\r\n")
            if zeile:
                if zeile.startswith("data:"):
                    zeilen.append(zeile[5:].lstrip())
                continue
            daten, zeilen = "\n".join(zeilen), []
            if not daten:
                continue
            if daten == "[DONE]":
                return
            try:
                stueck = json.loads(daten)
            except ValueError:
                continue
            if isinstance(stueck, dict) and stueck.get("error"):
                fehler = stueck["error"] if isinstance(stueck["error"], dict) else {}
                try:
                    status = int(fehler.get("status") or 500)
                except (TypeError, ValueError):
                    status = 500
                raise api_error(status, stueck)
            yield stueck
    finally:
        antwort.close()

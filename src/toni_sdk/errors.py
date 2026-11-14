"""Fehler des Toni SDK."""
from __future__ import annotations

from typing import Any, Optional


class ToniError(Exception):
    """Basis aller Fehler dieses Pakets."""


class ToniConnectionError(ToniError):
    """Keine Antwort: Netzwerkfehler oder Zeitgrenze."""


class ToniApiError(ToniError):
    """Die API hat mit einem Fehler geantwortet (HTTP 4xx/5xx)."""

    def __init__(self, status: int, body: Any, fallback: str) -> None:
        e = body.get("error") if isinstance(body, dict) else None
        e = e if isinstance(e, dict) else {}
        message = e.get("message")
        super().__init__(message if isinstance(message, str) and message else fallback)
        #: HTTP-Status
        self.status: int = status
        #: z. B. invalid_request_error, permission_error, rate_limit_error
        self.type: Optional[str] = e.get("type")
        #: Stabiler Schlüssel zum Auswerten, z. B. recht_fehlt, insufficient_quota, bestaetigung_fehlt
        self.code: Optional[str] = e.get("code")
        #: Betroffenes Feld, falls benennbar
        self.param: Optional[str] = e.get("param")
        #: Antwort im Rohzustand
        self.body: Any = body


class AuthenticationError(ToniApiError):
    """401 — Schlüssel fehlt oder ist ungültig."""


class InsufficientCreditError(ToniApiError):
    """402 — Guthaben aufgebraucht."""


class PermissionError(ToniApiError):  # noqa: A001 - bewusst wie in den anderen SDKs benannt
    """403 — dem Schlüssel fehlt ein Recht oder eine Stufe."""


class ConfirmationRequiredError(ToniApiError):
    """409 — ``loeschen``/``veroeffentlichen`` ohne Bestätigung."""


class RateLimitError(ToniApiError):
    """429 — zu viele Anfragen oder Monatslimit."""


_KLASSEN = {
    401: AuthenticationError,
    402: InsufficientCreditError,
    403: PermissionError,
    409: ConfirmationRequiredError,
    429: RateLimitError,
}


def api_error(status: int, body: Any) -> ToniApiError:
    return _KLASSEN.get(status, ToniApiError)(status, body, f"Die Toni API hat mit HTTP {status} geantwortet.")

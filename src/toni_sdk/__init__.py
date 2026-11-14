"""Toni SDK für Python — https://ki-markt.com"""
from ._generated import API_VERSION, catalog
from ._http import DEFAULT_BASE_URL, VERSION
from .agent import Agent, AgentResult, AgentStep, PendingCall, Tool, Toolbox
from .client import Platform, Toni
from .errors import (
    AuthenticationError,
    ConfirmationRequiredError,
    InsufficientCreditError,
    PermissionError,
    RateLimitError,
    ToniApiError,
    ToniConnectionError,
    ToniError,
)

__version__ = VERSION

__all__ = [
    "Toni", "Platform", "Agent", "AgentResult", "AgentStep", "PendingCall", "Tool", "Toolbox",
    "ToniError", "ToniApiError", "ToniConnectionError", "AuthenticationError", "InsufficientCreditError",
    "PermissionError", "ConfirmationRequiredError", "RateLimitError",
    "catalog", "API_VERSION", "VERSION", "DEFAULT_BASE_URL", "__version__",
]

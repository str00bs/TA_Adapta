"""
Module contains API Responses that are:
- Derived from the API Schema
- Used by the API Routers and endpoint controllers
- Used to generate openapi.json, SwaggerUI and ReDoc
"""

from .generic import GenericResponses
from .system import SystemResponses

__all__ = [
    "GenericResponses",
    "SystemResponses",
]

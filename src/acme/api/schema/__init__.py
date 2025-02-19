"""
Module contains API Schema that are:
- Used by routers to parse and validate inbound & outbound requests
- Used by responses to generate openapi.json, SwaggerUI and ReDoc
"""

from .generic import MessageSchema, MetaSchema

__all__ = [
    "MessageSchema",
    "MetaSchema",
]

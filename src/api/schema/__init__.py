"""
Module contains API Schema that are:
- Used by routers to parse and validate inbound & outbound requests
- Used by responses to generate openapi.json, SwaggerUI and ReDoc
"""

from .generic import MetaSchema, ResponseSchema
from .messages import MessagesList, MessagesSchema
from .users import UsersList, UsersSchema, UsersType

__all__ = [
    "MetaSchema",
    "ResponseSchema",
    "MessagesList",
    "MessagesSchema",
    "UsersList",
    "UsersSchema",
    "UsersType",
]

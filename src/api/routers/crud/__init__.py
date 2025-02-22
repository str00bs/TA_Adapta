"""
Module contains routers and endpoints controllers used specifically for:
- `CREATE`, `RETRIEVE`, `UPDATE` and `DELETE` entity operations.
"""

from fastapi import APIRouter

from .messages import router as MessagesRouter
from .users import router as UsersRouter

crud_routers: list[APIRouter] = [
    MessagesRouter,
    UsersRouter,
]

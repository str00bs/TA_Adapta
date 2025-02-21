"""
Module contains database ORM models
? Doc Reference: https://orm.masoniteproject.com/models
"""

from .messages import MessagesModel
from .users import UsersModel

__all__ = [
    "MessagesModel",
    "UsersModel",
]

"""
Module contains database (event) observers
? Doc reference: https://orm.masoniteproject.com/models?q=obsrvers
"""

from .messages import MessagesObserver
from .users import UsersObserver

__all__ = ["MessagesObserver", "UsersObserver"]

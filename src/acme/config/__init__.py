"""Module contains app, auth and database configurations"""

from .api import APIConfig
from .auth import AuthConfig
from .databases import DatabaseConfig

__all__ = ["APIConfig", "AuthConfig", "DatabaseConfig"]


class Config:
    """Contains *all* configurations"""

    API: APIConfig = APIConfig()
    Auth: AuthConfig = AuthConfig()
    DB: DatabaseConfig = DatabaseConfig()

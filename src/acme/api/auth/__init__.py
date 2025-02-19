"""Module contains API (basic) Auth implementation"""

import secrets

from config import Config
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


class AuthMethods:
    """Contains various methods of Authentication"""

    basic: HTTPBasic = HTTPBasic(
        scheme_name="basic",
        description="Basic Auth",
        realm=None,
        auto_error=True,
    )


class Auth:
    """Contains all auth implementations"""

    @staticmethod
    def basic(credentials: HTTPBasicCredentials = Depends(AuthMethods.basic)):
        """Basic Auth validation method against configured credentials"""
        valid_credentials = all(
            [
                secrets.compare_digest(
                    credentials.username.encode("utf8"),
                    Config.Auth.username.encode("utf8"),
                ),
                secrets.compare_digest(
                    credentials.password.encode("utf8"),
                    Config.Auth.password.encode("utf8"),
                ),
            ]
        )
        if not valid_credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )

        return credentials.username

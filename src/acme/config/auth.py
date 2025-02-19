"""File contains Auth Configuration"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthConfig(BaseSettings):
    """Loads, parses and validates Auth configuration"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="AUTH_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    username: str = Field("admin", description="Basic Auth - Username")
    password: str = Field("admin", description="Basic Auth - Password")

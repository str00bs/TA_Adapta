"""File contains Database(s) Configuration(s)"""

from pathlib import Path

from masoniteorm.connections import ConnectionResolver
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    """Loads, parses and validates Database configuration"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    host: str | None = Field(None)
    port: int | None = Field(None)
    database: str | Path = Field(...)

    driver: str = Field(...)
    driver_default: str = Field(...)
    log_queries: bool | None = Field(None)

    user: str = Field(...)
    password: str = Field(...)

    def to_orm_format(self) -> dict:
        """Method parses configuration to MasoniteORM's expected format"""
        data = self.model_dump()
        default_driver = data.pop("driver_default")
        return {"default": default_driver, default_driver: data}


# ? This instantiates the DB connection with the DatabaseConfig
DB = ConnectionResolver().set_connection_details(DatabaseConfig().to_orm_format())

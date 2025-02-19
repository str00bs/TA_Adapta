"""File contains API Configuration"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class APIConfig(BaseSettings):
    """Loads, parses and validates API configuration"""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="API_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    title: str = Field(..., description="API Title")
    description: str = Field(..., description="API Description")
    version: str = Field(..., description="API Version")
    authors: list[str] = Field(..., description="API Authors")
    openapi_url: str = Field(..., description="API OpenAPI URL")
    debug: bool = Field(..., description="API Debug Mode")

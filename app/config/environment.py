"""Environment configuration module."""

from typing import Set

from app.config.types import BaseSettings
from pydantic import Field


class CORSSettings(BaseSettings):
    """Web server CORS settings."""

    allow_credentials: bool = Field(True, env="CORS_ALLOW_CREDENTIALS")
    allow_headers: Set[str] = Field(["*"], env="CORS_ALLOW_HEADERS")
    allow_methods: Set[str] = Field(["*"], env="CORS_ALLOW_METHODS")
    allow_origins: Set[str] = Field(["*"], env="CORS_ALLOW_ORIGINS")


class WebAppSettings(BaseSettings):
    """Web application settings."""

    debug: bool = Field(env="WEB_APP_DEBUG")
    description: str = Field(env="WEB_APP_DESCRIPTION")
    title: str = Field(env="WEB_APP_TITLE")
    version: str = Field(env="WEB_APP_VERSION")


class WebServerSettings(BaseSettings):
    """Web server settings."""

    host: str = Field(env="WEB_SERVER_HOST")
    port: int = Field(env="WEB_SERVER_PORT")
    reload: bool = Field(env="WEB_SERVER_RELOAD")


class Settings(BaseSettings):
    """Environment settings."""

    cors_settings: CORSSettings = CORSSettings()
    web_app_settings: WebAppSettings = WebAppSettings()
    web_server_settings: WebServerSettings = WebServerSettings()

    env: str = Field(env="ENV")
    log_level: str = Field(env="LOG_LEVEL")
    python_path: str = Field(env="PYTHONPATH")

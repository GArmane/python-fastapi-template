"""Application description here."""

__all__ = ("init_app",)

import uvicorn
from fastapi.applications import FastAPI

from app.api.app import init_app
from app.config.environment import Settings


def _get_settings() -> Settings:
    return Settings()


def start_application() -> FastAPI:
    """Start FastAPI application."""
    return init_app(_get_settings())


def start_web_server():
    """Start Uvicorn web server."""
    settings = _get_settings()

    uvicorn.run(
        "app:start_application",
        host=settings.web_server_settings.host,
        port=settings.web_server_settings.port,
        reload=settings.web_server_settings.reload,
        log_level=settings.log_level,
        factory=True,
    )

"""CORS Middleware module."""

from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dependency_injector.wiring import inject, Provide
from app.core.container import Container
from typing import Any


@inject
def configure_cors(
    app: FastAPI,
    settings: dict[str, Any] = Provide[Container.config],
) -> FastAPI:
    """Configure CORS middleware."""
    cors_settings = settings["cors_settings"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_settings["allow_origins"],
        allow_credentials=cors_settings["allow_credentials"],
        allow_methods=cors_settings["allow_methods"],
        allow_headers=cors_settings["allow_headers"],
    )
    return app

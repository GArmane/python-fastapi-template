"""Dependency injection module."""

from typing import Any

from app.config.environment import Settings
from app.core.httpx import init_http_client
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration


class Container(DeclarativeContainer):
    """Base DI container."""

    config = Configuration()
    http_client = providers.Resource(init_http_client)


def create_container(settings: Settings, modules: list[Any]) -> Container:
    """Create a Conteiner."""
    container = Container()
    container.config.from_pydantic(settings, required=True)
    container.wire(modules=modules)

    return container

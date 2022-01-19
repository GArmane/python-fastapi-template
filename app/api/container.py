"""Dependency injection module."""

from typing import AsyncGenerator

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration
from httpx import AsyncClient


async def init_http_client() -> AsyncGenerator[AsyncClient, None]:
    """Initialize HTTPX Client and close it when finished."""
    client = AsyncClient()
    yield client
    await client.aclose()


class Container(DeclarativeContainer):
    """Base DI container."""

    config = Configuration()
    http_client = providers.Resource(init_http_client)

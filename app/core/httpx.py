"""HTTPX module."""

from httpx import AsyncClient
from typing import AsyncGenerator


async def init_http_client() -> AsyncGenerator[AsyncClient, None]:
    """Initialize HTTPX Client and close it when finished."""
    client = AsyncClient()
    yield client
    await client.aclose()

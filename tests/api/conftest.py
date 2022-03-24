"""API tests conftest module."""

import pytest
import pytest_asyncio
from app.api.app import init_app
from fastapi.testclient import TestClient
from httpx import AsyncClient


@pytest_asyncio.fixture()
async def async_test_client(web_app):
    """Return an async test client."""
    async with AsyncClient(app=web_app, base_url="http://") as ac:
        yield ac


@pytest.fixture()
def web_app(env_settings):
    """Return web application instance."""
    return init_app(env_settings)


@pytest.fixture()
def test_client(web_app):
    """Return web application test client."""
    return TestClient(web_app)

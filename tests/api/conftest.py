"""API tests conftest module."""

import pytest
from fastapi.testclient import TestClient
from app.api.app import init_app
from httpx import AsyncClient


@pytest.fixture()
def web_app(env_settings):
    """Return web application instance."""
    return init_app(env_settings)


@pytest.fixture()
def test_client(web_app):
    """Return web application test client."""
    return TestClient(web_app)


@pytest.fixture()
async def async_test_client(web_app):
    """Return an async test client."""
    async with AsyncClient(app=web_app, base_url="http://") as ac:
        yield ac

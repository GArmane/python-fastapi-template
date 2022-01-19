"""API tests conftest module."""

import pytest
from fastapi.testclient import TestClient
from app.api.app import init_app


@pytest.fixture()
def web_app(env_settings):
    """Return web application instance."""
    return init_app(env_settings)


@pytest.fixture()
def test_client(web_app):
    """Return web application test client."""
    return TestClient(web_app)

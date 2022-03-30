"""Core tests conftest module."""

import pytest
from app.core.container import create_container


@pytest.fixture()
def di_container(env_settings):
    """Return standalone DI container."""
    return create_container(env_settings)

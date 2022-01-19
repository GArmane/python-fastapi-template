"""General conftest module for all tests."""

import pytest
from app.config.environment import Settings


@pytest.fixture()
def env_settings():
    """Return environment settings."""
    return Settings()


@pytest.fixture()
def mock_function(mocker):
    """Mock function fixture function.

    Returns fixture that generates a callable mock object.
    """
    return lambda name, return_value: mocker.MagicMock(
        name=name,
        return_value=return_value,
    )


@pytest.fixture()
def mock_module(mocker):
    """Mock module fixture function.

    Returns fixture that is capable of generating a mock object that implements all
    attributes and methods from a given spec.
    """
    return lambda name, spec: mocker.Mock(name=name, spec=spec)

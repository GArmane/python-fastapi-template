"""General conftest module for all tests."""

import pytest
from app.config.environment import Settings
from xdist import is_xdist_worker


@pytest.fixture(scope="session")
def env_settings(master_env_settings, request):
    """Return current node environment settings."""
    if is_xdist_worker(request):
        # If running tests in a pytest-xdist environment, you can customize env
        # variables here. These variables are isolated between nodes.
        custom_vars = {}
        return Settings(**custom_vars)

    return master_env_settings


@pytest.fixture(scope="session")
def master_env_settings():
    """Return master node environment settings."""
    return Settings()


@pytest.fixture()
def mock_class(mocker):
    """Mock class fixture function.

    Returns fixture that is capable of generating a mock object that implements all
    attributes and methods from a given spec.
    """
    return lambda name, spec: mocker.Mock(name=name, spec=spec)


@pytest.fixture()
def mock_function(mocker):
    """Mock function fixture function.

    Returns fixture that generates a callable mock object.
    """
    return lambda name, return_value: mocker.MagicMock(
        name=name,
        return_value=return_value,
    )

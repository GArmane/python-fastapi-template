"""FastAPI application main module.

Implements DI container initialization, FastAPI application instantiation,
event handling, middleware and route registry.
"""

from app.config.environment import Settings

import app.api.middlewares.cors as cors
import app.api.routers.public as public_router
from app.api.container import Container
from app.api.error_handlers import register_error_handlers as _register_error_handlers
from fastapi.applications import FastAPI
from toolz import pipe


def _create_container(settings: Settings) -> Container:
    """Create and initialize base container for the dependency injection mechanism."""
    container = Container()
    container.config.from_pydantic(settings, required=True)
    container.wire(
        modules=[
            cors,
            public_router,
        ],
    )
    return container


def _create_instance(container: Container) -> FastAPI:
    """Create and perform base initialization of the FastAPI application."""
    web_app_settings = container.config.web_app_settings

    app: FastAPI = FastAPI(
        debug=web_app_settings.debug(),
        title=web_app_settings.title(),
        description=web_app_settings.description(),
        version=web_app_settings.version(),
    )
    app.container = container  # type:ignore

    return app


def _register_events(app: FastAPI) -> FastAPI:
    """Register event handlers.

    Register event handlers that need to be executed before the application starts up,
    or when the application shuts down.
    """
    return app


def _register_middlewares(app: FastAPI) -> FastAPI:
    """Register middlewares to be executed in the request/response application cycle."""
    app = pipe(
        app,
        cors.configure_cors,
    )
    return app


def _register_routers(app: FastAPI) -> FastAPI:
    """Register APIRouters with the FastAPI application."""
    app.include_router(public_router.router)
    return app


def init_app(settings: Settings) -> FastAPI:
    """Initialize FastAPI application instance."""
    app: FastAPI = pipe(
        settings,
        _create_container,
        _create_instance,
        _register_events,
        _register_middlewares,
        _register_routers,
        _register_error_handlers,
    )
    return app

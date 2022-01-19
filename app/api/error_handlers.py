"""Custom exception handlers are defined here."""
from fastapi.applications import FastAPI


def register_error_handlers(app: FastAPI) -> FastAPI:
    """Register event handlers.

    Register error handlers that need to be executed when certain errors are thrown by
    router handlers.
    """
    return app

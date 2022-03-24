"""Custom exception handlers."""

from typing import Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.types import ErrorResponse


def _handle_validation_error(
    _: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Override fastapi.RequestValidationException with simpler format."""
    return JSONResponse(
        content=ErrorResponse(detail=exc.errors(), message="Validation error").dict(),
        status_code=400,
    )


def register_error_handlers(app: FastAPI) -> FastAPI:
    """Register event handlers.

    Register error handlers that need to be executed when certain errors are thrown by
    router handlers.
    """
    handler_map = {
        RequestValidationError: _handle_validation_error,
    }

    for exc_class, handler in handler_map.items():
        app.add_exception_handler(exc_class, handler)

    return app


def render_error(
    status_code: int,
    detail: dict[str, Any] | None,
    msg: str | None = None,
) -> JSONResponse:
    """Format API errors."""
    if not msg:
        match status_code:
            case 400:
                msg = "Bad Request"
            case 401:
                msg = "Unauthorized"
            case 403:
                msg = "Forbidden"
            case 404:
                msg = "Not Found"
            case _:
                msg = "Error"

    return JSONResponse(
        content=ErrorResponse(detail=jsonable_encoder(detail), message=msg).dict(),
        status_code=status_code,
    )

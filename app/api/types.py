"""Shared API types."""
from typing import Generic, TypeVar

from app.core.types import GenericSchema

GenericData = TypeVar("GenericData")


class ErrorResponse(GenericSchema, Generic[GenericData]):
    """Generic error response for unsuccesful requests.

    Unsuccesful response are only response in the 400 HTTP status codes.
    500 HTTP status code is considered a server problem,
    threfore, a bug and must be fixed instead of treated and returned to the user.

    :param detail: details about the error.
    :param message: human readable message about the error.
    """

    detail: GenericData | None
    message: str

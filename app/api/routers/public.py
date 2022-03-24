"""Public router module."""

from enum import Enum
from typing import Any

from app.core.container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status
from fastapi.routing import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/public")


class StatusEnum(str, Enum):
    """Status enum defining all possible health status for the API.

    StatusEnum.OK: API is fully functional and operational.
    """

    OK = "OK"


class HealthCheck(BaseModel):
    """Health check route response class."""

    title: str = Field(..., description="API title")
    description: str = Field(..., description="Brief description of the API")
    version: str = Field(..., description="API semver version number")
    status: StatusEnum = Field(..., description="API current status")


@router.get(
    "/status",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    tags=["Health Check"],
)
@inject
def health_check(
    settings: dict[str, Any] = Depends(Provide[Container.config]),
) -> dict[str, str]:
    """Perform health check.

    Performs health check and returns information about the running service.
    """
    web_app_settings = settings["web_app_settings"]
    return {
        "title": web_app_settings["title"],
        "description": web_app_settings["description"],
        "version": web_app_settings["version"],
        "status": StatusEnum.OK,
    }

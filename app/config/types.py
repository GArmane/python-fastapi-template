"""Config module types."""

from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    """Base Settings class for application."""

    class Config:
        """Model config."""

        allow_mutation = False

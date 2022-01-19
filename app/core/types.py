"""This module defines various types used by the core application."""

__all__ = ("GenericSchema", "Schema")

from enum import Enum as BaseEnum

from pydantic import BaseModel
from pydantic.generics import GenericModel


class Enum(str, BaseEnum):
    """Base generic enum class for application models."""

    def __str__(self):
        return self.value


class GenericSchema(GenericModel):
    """Base generic schema class for application models."""

    class Config:
        """Schema configuration."""

        allow_mutation = False


class Schema(BaseModel):
    """Base schema class for application models."""

    class Config:
        """Schema configuration."""

        allow_mutation = False

#!/usr/bin/python3
"""Defines the amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init constructor"""
        super().__init__(self, *args, **kwargs)

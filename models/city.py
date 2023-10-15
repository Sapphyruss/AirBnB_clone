#!/usr/bin/python3
"""Defines the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Allow the City class to inherit
    and utilize the behavior and attributes
    defined in the BaseModel class."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """The init Constructor"""
        super().__init__(self, *args, **kwargs)

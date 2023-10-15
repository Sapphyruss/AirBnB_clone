#!/usr/bin/python3
"""Define sthe review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review"""
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """__init Constructor"""
        super().__init__(self, *args, **kwargs)

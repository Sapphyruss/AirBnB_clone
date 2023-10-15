#!/usr/bin/python3
"""BaseModel Class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Ininitialize the new BaseModel.
        Args:
            *args : wont be used.
            **kwargs (dict) : Key, value of attributes.
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        clssname = self.__class__.__name__
        return "[{}] ({}) {}".format(clssname, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the instant datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary will all keys and values of the instance."""
        bmdict = self.__dict__.copy()
        bmdict["created_at"] = self.created_at.isoformat()
        bmdict["updated_at"] = self.updated_at.isoformat()
        bmdict["__class__"] = self.__class__.__name__
        return bmdict

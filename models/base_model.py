#!/usr/bin/python3
"""BaseModel Class."""
import models
import datetime
from uuid import uuid4


class BaseModel:
    """Defines the class BaseModel."""

    def __init__(self, *args, **kwargs):
        """Ininitialize the new BaseModel.
        Args:
            **kwargs (dict) : Key, value of attributes.
        """
        tformat = '%Y-%m-%dT%H:%M:%S.%f'
        for k, v in kwargs.items():
            if k == "created_at":
                v = datetime.strptime(value, tformat)
            if k == "updated_at":
                v = datetime.strptime(value, tformat)
            if k != "__class__":
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        bmdict["updated_at"] = self.created_at.isoformat()
        bmdict["__class__"] = self.__class__.__name__
        return bmdict

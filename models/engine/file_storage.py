#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """Storage engine.
    Attr:
        __file_path : File to save objects in.
        __objects : A dict of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __object to the JSON file __file_path."""
        fsdict = FileStorage.__objects
        objdict = {obj: fsdict[obj].to_dict() for obj in fsdict.keys()}
        with open(FileStorage.__file_path, "w" ) as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass

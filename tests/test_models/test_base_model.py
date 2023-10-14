#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the class BaseModel"""

    def test_init_BaseModel(self):
        """test object type in BaseModel"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_id(self):
        """ test if the Id is uniaue """
        my_objectId = BaseModel()
        my_objectId1 = BaseModel()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        """test the output fromat"""
        my_strobject = BaseModel()
        _dict = my_strobject.__dict__
        str1 = "[BaseModel] ({}) {}".format(my_strobject.id, _dict)
        str2 = str(my_strobject)
        self.assertEqual(str1, str2)

    def test_save(self):
        """test if the date is upfated after save"""
        my_objectupdate = BaseModel()
        first_updated = my_objectupdate.updated_at
        my_objectupdate.save()
        second_updated = my_objectupdate.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """test if to_dict returns a dictionary"""
        my_modell = BaseModel()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for k, v in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for k, v in my_dict_modell.items():
            if k == 'created_at':
                self.assertIsInstance(value, str)
            if k == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()

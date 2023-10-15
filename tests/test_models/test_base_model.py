#!/usr/bin/python3
""" Unittest of BaseModel """

import unittest
import os
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test the class BaseModel"""

    def test_docstring(self):
        """test if docstring is there"""
        txt = "No docstring for this mosule"
        self.assertIsNotNone(models.base_model.__doc__, txt)
        txt = "No docstring for this class"
        self.assertIsNotNone(BaseModel.__doc__, txt)

    def test_init_BaseModel(self):
        """test object"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_id(self):
        """test id the id is unique """
        my_objectId = BaseModel()
        my_objectId1 = BaseModel()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_str(self):
        """test str output"""
        my_strobject = BaseModel()
        _dict = my_strobject.__dict__
        string1 = "[BaseModel] ({}) {}".format(my_strobject.id, _dict)
        string2 = str(my_strobject)
        self.assertEqual(string1, string2)

    def test_save(self):
        """test update after save"""
        my_objectupdate = BaseModel()
        first_updatedate = my_objectupdate.updated_at
        my_objectupdate.save()
        second_updated = my_objectupdate.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """test to_dict becomes a dictionary"""
        my_modell = BaseModel()
        my_dict_modell = my_modell.to_dict()
        self.assertIsInstance(my_dict_modell, dict)
        for key, value in my_dict_modell.items():
            flag = 0
            if my_dict_modell['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for k, v in my_dict_modell.items():
            if k == 'created_at':
                self.assertIsInstance(v, str)
            if k == 'updated_at':
                self.assertIsInstance(v, str)


if __name__ == '__main__':
    unittest.main()

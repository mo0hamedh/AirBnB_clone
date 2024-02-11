#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import models


class TestFileStorage(unittest.TestCase):
    """
    Test class for FileStorage
    """
    my_storage = FileStorage()
    base_obj = BaseModel()
    my_storage.new(base_obj)
    objs = my_storage.all()
    my_storage.save()  # this saved it to file.json
    cls_name = "BaseModel"
    instance_id = base_obj.id
    keyname = "BaseModel."+instance_id
    filepath = models.storage._FileStorage__file_path
    _objects = models.storage._FileStorage__objects

    def test_filestorage(self):
        """
        create an instance of class withexpected kwargs
        """
        self.assertEqual(self.filepath, "file.json")
        self.assertIsInstance(self.filepath, str)
        self.assertIsInstance(self._objects, dict)
        self.assertIsInstance(self.my_storage.all(), dict)
        self.assertIsInstance(self.objs[self.keyname], BaseModel)
        self.assertTrue(hasattr(self.base_obj, 'id'))
        self.assertIsInstance(self.base_obj.id, str)
        self.assertTrue(hasattr(self.base_obj, "__init__"))
        self.assertTrue(hasattr(self.base_obj, "__str__"))
        self.assertTrue(hasattr(self.base_obj, "save"))
        self.assertTrue(hasattr(self.base_obj, "to_dict"))

    def test_new_all_methods(self):
        """Testing new and all methods"""
        obj = self.objs[self.keyname]
        self.assertEqual(obj, self.base_obj)
        self.assertIsInstance(self.objs, dict)
        self.assertNotEqual(self.objs, {})

    def test_save_method(self):
        """Testing save method"""
        with open('file.json', 'r', encoding='utf-8') as f:
            json_objects = json.load(f)
        json_obj = json_objects[self.keyname]
        self.assertIn(self.keyname, json_objects)
        self.assertEqual(json_obj, self.base_obj.to_dict())

    def test_z_reload_method(self):
        """
        Testing reload method
        added z to method name to run last
        """
        self.objs.clear()
        self.my_storage.reload()
        with open('file.json', 'r', encoding='utf-8') as f:
            json_objects = json.load(f)
        self.assertEqual(json_objects[self.keyname],
                         self.objs[self.keyname].to_dict())

#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


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

    def test_filestorage(self):
        """
        create an instance of class withexpected kwargs
        """
        self.assertIsInstance(self.my_storage.all(), dict)

    def test_new_all_methods(self):
        """Testing new and all methods"""
        obj = self.objs[f"{self.cls_name}.{self.instance_id}"]
        self.assertEqual(obj, self.base_obj)

    def test_save_method(self):
        """Testing save method"""
        with open('file.json', 'r', encoding='utf-8') as f:
            json_objects = json.load(f)
            json_obj = json_objects[self.keyname]
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
        """for k, v in json_objects.items():
            cls = v['__class__']
            self.assertEqual(str(self.objs[k]), str(
                eval(f"{cls}(**{v})")))
        self.assertEqual(str(self.base_obj), str(
            eval(f"{self.cls_name}(**{self.base_obj}.to_dict()")))
        """

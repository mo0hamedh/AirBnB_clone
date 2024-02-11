#!/usr/bin/python3
"""
Unittest for base model
"""
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel Class
    """

    def setUp(self):
        """Creating instance for my tests"""
        print(f"Setting Up Instance of BaseModel for {self._testMethodName}")
        self.obj = BaseModel()
        self.obj.name = "My_First_Model"
        self.obj.my_number = 89

    def test_basemodel_no_kwargs(self):
        """
        create an instance of class withexpected kwargs
        """
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.name, "My_First_Model")
        self.assertEqual(self.obj.my_number, 89)

    def test_basemodel_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        kwargs = self.obj.to_dict()
        new_obj = BaseModel(**kwargs)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertIsInstance(new_obj.id, str)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)
        self.assertEqual(new_obj.name, "My_First_Model")
        self.assertEqual(new_obj.my_number, 89)
        self.assertNotEqual(new_obj, self.obj)

    def test_string_representation(self):
        """
        Testing __str__ method
        """
        self.assertEqual(
            f"[BaseModel] ({self.obj.id}) {self.obj.__dict__}", str(self.obj))

    def test_save(self):
        """
        Testing save method
        """
        time_before_save = self.obj.updated_at
        self.obj.save()
        self.assertGreater(self.obj.updated_at, time_before_save)

    def test_to_dict_method(self):
        """
        Testing to_dict() method
        """
        method_dict = self.obj.to_dict()
        expected_dict = self.obj.__dict__.copy()
        expected_dict["__class__"] = self.obj.__class__.__name__
        expected_dict["created_at"] = self.obj.created_at.isoformat()
        expected_dict["updated_at"] = self.obj.updated_at.isoformat()
        self.assertDictEqual(method_dict, expected_dict)

#!/usr/bin/python3
"""
Unittest for City model
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testing class for City module"""

    def test_default_values(self):
        """Testing default value of City"""
        obj = City()
        self.assertEqual(obj.state_id, '')
        self.assertEqual(obj.name, '')

#!/usr/bin/python3
"""
Unittest for Amenity model
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing class for Amenity module"""

    def test_default_values(self):
        """Testing default value of amenity"""
        obj = Amenity()
        self.assertEqual(obj.name, '')

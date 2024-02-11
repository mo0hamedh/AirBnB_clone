#!/usr/bin/python3
"""
Unittest for Placesd model
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing class for Place module"""

    def test_default_values(self):
        """Testing default value of Place"""
        obj = Place()
        self.assertEqual(obj.name, '')
        self.assertEqual(obj.city_id, '')
        self.assertEqual(obj.user_id, '')
        self.assertEqual(obj.description, '')
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

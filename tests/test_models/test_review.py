#!/usr/bin/python3
"""
Unittest for Review model
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing class for Review module"""

    def test_default_values(self):
        """Testing default value of amenity"""
        obj = Review()
        self.assertEqual(obj.place_id, '')
        self.assertEqual(obj.user_id, '')
        self.assertEqual(obj.text, '')

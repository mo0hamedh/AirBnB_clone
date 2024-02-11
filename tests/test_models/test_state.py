#!/usr/bin/python3
"""
Unittest for State model
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing class for State module"""

    def test_default_values(self):
        """Testing default value of amenity"""
        obj = State()
        self.assertEqual(obj.name, '')

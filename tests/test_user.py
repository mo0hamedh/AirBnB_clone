#!/usr/bin/python3
"""
Unittest for User model
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing class for User module"""

    def test_default_values(self):
        """Testing default value of User"""
        obj = User()
        self.assertEqual(obj.last_name, '')
        self.assertEqual(obj.first_name, '')
        self.assertEqual(obj.email, '')
        self.assertEqual(obj.password, '')

#!/usr/bin/python3
"""
This script initializes a FileStorage instance and reloads data,
making it available for managing and persisting data.
"""


import io
import sys
import unittest
import os
import datetime
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """
    This script initializes a FileStorage instance and reloads data,
    making it available for managing and persisting data.
    """

    def test_attributes(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base1 = User()
        base2 = User()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base1 = User()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_email(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base = User()
        self.assertEqual(base.email, "")

    def test_password(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base = User()
        self.assertEqual(base.password, "")

    def test_user_first_name_last_name(self):
        """
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        """

        base = User()
        self.assertEqual(base.first_name, "")
        self.assertEqual(base.last_name, "")

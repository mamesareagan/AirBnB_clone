#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    def setUp(self):
        """Set up test instance before each test case."""
        self.user = User()

    def tearDown(self):
        """Clean up after each test case."""
        del self.user

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_init(self):
        self.assertIsInstance(self.user, User)

    def test_two_models_are_unique(self):
        user2 = User(email="a", password="a")
        self.assertNotEqual(self.user.id, user2.id)
        self.assertLess(self.user.created_at, user2.created_at)
        self.assertLess(self.user.updated_at, user2.updated_at)

    def test_init_args_kwargs(self):
        dt = datetime.utcnow()
        user2 = User("1", id="5", created_at=dt.isoformat())
        self.assertEqual(user2.id, "5")
        self.assertEqual(user2.created_at, dt)

    def test_str(self):
        s = str(self.user)
        self.assertIn("'id': '{}'".format(self.user.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.user.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.user.updated_at)), s)

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(dict, type(user_dict))
        self.assertEqual(self.user.id, user_dict["id"])
        self.assertEqual("User", user_dict["__class__"])
        self.assertEqual(self.user.created_at.isoformat(),
                         user_dict["created_at"])
        self.assertEqual(self.user.updated_at.isoformat(),
                         user_dict["updated_at"])


if __name__ == "__main__":
    unittest.main()

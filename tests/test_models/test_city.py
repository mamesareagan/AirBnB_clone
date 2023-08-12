#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    def setUp(self):
        """Set up test instance before each test case."""
        self.city = City()

    def tearDown(self):
        """Clean up after each test case."""
        del self.city

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        ct = City()
        self.assertEqual(str, type(ct.id))
        self.assertEqual(datetime, type(ct.created_at))
        self.assertEqual(datetime, type(ct.updated_at))
        self.assertTrue(hasattr(ct, "name"))
        self.assertTrue(hasattr(ct, "state_id"))

    def test_is_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_init(self):
        self.assertIsInstance(self.city, City)

    def test_two_models_are_unique(self):
        ct = City()
        self.assertNotEqual(self.city.id, ct.id)
        self.assertLess(self.city.created_at, ct.created_at)
        self.assertLess(self.city.updated_at, ct.updated_at)

    def test_init_args_kwargs(self):
        dt = datetime.utcnow()
        ct = City("1", id="5", created_at=dt.isoformat())
        self.assertEqual(ct.id, "5")
        self.assertEqual(ct.created_at, dt)

    def test_str(self):
        s = str(self.city)
        self.assertIn("'id': '{}'".format(self.city.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.city.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.city.updated_at)), s)
        
    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(dict, type(city_dict))
        self.assertEqual(self.city.id, city_dict["id"])
        self.assertEqual("City", city_dict["__class__"])
        self.assertEqual(self.city.created_at.isoformat(),
                         city_dict["created_at"])
        self.assertEqual(self.city.updated_at.isoformat(),
                         city_dict["updated_at"])
        
if __name__ == "__main__":
    unittest.main()


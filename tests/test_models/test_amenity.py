#!/usr/bin/python3
"""Defines unittests for Amenity class."""
import pep8
from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity class."""

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instance_creation(self):
        """Test instance creation."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()

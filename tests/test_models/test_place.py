#!/usr/bin/python3
"""Defines unittests for Place class."""
import pep8
from models.base_model import BaseModel
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for Place class."""

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/place.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instance_creation(self):
        """Test instance creation."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test attributes."""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_default_values(self):
        """Test default values."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])

    def test_setting_values(self):
        """Test setting attribute values."""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Luxury Villa"
        place.description = "A beautiful villa by the sea"
        place.number_rooms = 5
        place.number_bathrooms = 4
        place.max_guest = 10
        place.price_by_night = 200
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["amenity1", "amenity2"]
        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Luxury Villa")
        self.assertEqual(place.description, "A beautiful villa by the sea")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 4)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 200)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == "__main__":
    unittest.main()

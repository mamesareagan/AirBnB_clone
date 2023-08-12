#!/usr/bin/python3
"""Defines unittests for Review class."""
import pep8
from models.base_model import BaseModel
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unittests for Review class."""
    
    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")
    
    def test_instance_creation(self):
        """Test instance creation."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
    
    def test_attributes(self):
        """Test attributes."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
    
    def test_default_values(self):
        """Test default values."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
    
    def test_setting_values(self):
        """Test setting attribute values."""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user123"
        review.text = "A fantastic experience!"
        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "A fantastic experience!")

if __name__ == "__main__":
    unittest.main()

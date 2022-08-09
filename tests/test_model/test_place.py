#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.place import Place
import pep8
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity class """

    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Place.__doc__)

    def test_instance_BaseModel(self):
        """ Tests inheritance """
        amenity = Place()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instaciacion(self):
        """ Tests correct instatiation of the class """
        am = Place()
        am.name = "Charlie"
        self.assertIn("name", am.to_dict())

    def test_to_dict(self):
        """ Tests that the function retrieves a dictionary """
        base = Place()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_str(self):
        """ Tests the str repr. of an object """
        base = Place()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_save(self):
        """ Tests the save method """
        base = Place()
        time1 = base.updated_at
        base.save()
        time2 = base.updated_at
        self.assertNotEqual(time1, time2)

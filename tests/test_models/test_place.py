#!/usr/bin/python3
""" Tests for place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models import place
import unittest
import pep8


class test_Place(test_basemodel):
    """ Class to add Unittests for Place class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Checks type """
        new = self.value(city_id="12345678s9")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Checks type """
        new = self.value(user_id="12345678s9")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Checks type """
        new = self.value(name="Betty Holberton")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Checks type """
        new = self.value(description="Woman")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Checks type """
        new = self.value(number_rooms=4)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Checks type """
        new = self.value(number_bathrooms=2)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Checks type """
        new = self.value(max_guest=8)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Checks type """
        new = self.value(price_by_night=3000)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Checks type """
        new = self.value(latitude=123456789.0)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Checks type """
        new = self.value(latitude=2.2)
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Checks type"""
        new = self.value(amenity_ids=["Wifi", "Tv", "AC"])
        self.assertEqual(type(new.amenity_ids), list)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDoc_place(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(place.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

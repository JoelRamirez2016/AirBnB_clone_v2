#!/usr/bin/python3
""" Tests for amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models import amenity
import unittest
import pep8


class test_Amenity(test_basemodel):
    """ Class to add Unittests for Amenity class """

    def __init__(self, *args, **kwargs):
        """ __init__ method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Checks type """
        new = self.value(name="Amenities")
        self.assertEqual(type(new.name), str)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDoc_amenity(unittest.TestCase):
    """ Class to check documentation in files. """
    def test_module_doc(self):
        """ Method to check for module documentation. """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_method_docs(self):
        """ Method to check for method´s documentation. """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)

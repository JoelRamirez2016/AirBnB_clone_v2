#!/usr/bin/python3
""" Tests for city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
import pep8


class test_City(test_basemodel):
    """ Class to add Unittests for City class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Checks type """
        new = self.value(state_id="12345687s9")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Checks type """
        new = self.value(name="Cali")
        self.assertEqual(type(new.name), str)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDoc_city:
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(city.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

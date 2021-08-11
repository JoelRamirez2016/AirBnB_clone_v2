#!/usr/bin/python3
""" Tests for state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import state
import unittest
import pep8


class test_state(test_basemodel):
    """ Class to add Unittests for Review class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Checks type """
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDoc_state(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(state.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)

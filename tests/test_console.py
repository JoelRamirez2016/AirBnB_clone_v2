""" Tests for console """
import unittest
import pep8
from models.base_model import BaseModel
from console import HBNBCommand
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import console


class TestConsole(unittest.TestCase):
    """ Unittests for the console """
    @classmethod
    def setUpClass(self):
        """Setup for the tests"""
        self.console = HBNBCommand()

    def tearDown(cls):
        """Cleaning up after each test"""
        pass

    def test_module_doc(self):
        """ Method to check for module documentation"""
        self.assertIsNotNone(console.__doc__)

    def test_class_docs(self):
        """ Method to check for class documentation."""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """ Method to check for method´s documentation."""
        for method in dir(HBNBCommand):
            self.assertIsNotNone(method.__doc__)


class TestCodeFormat(unittest.TestCase):
    """ Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

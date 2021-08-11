""" Tests for console """
import unittest
import pep8


class TestConsole(unittest.TestCase):
    """ Unittests for the console """
    def setUpClass(cls):
        """Setup for the tests"""
        cls.console = HBNBCommand()

    def tearDown(cls):
        """Cleaning up after each test"""
        del cls.console

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

""" Tests for db_storage """
import unittest
import pep8
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from unittest.case import skipIf
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "skip if not database")
class test_dbstorage(unittest.TestCase):
    """class to test the db storage methode"""
    def setUp(cls):
        """set up test env"""
        cls.user = User()
        cls.user.first_name = "Daniel"
        cls.user.last_name = "Ortega"
        cls.user.password = "pswd"
        cls.user.email = "orcha@gmail.com"
        cls.storage = FileStorage()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def testAll(self):
        """ Test-> all function in DBStorage """
        obj = storage.all()
        self.assertEqual(type(obj), dict)


class TestCodeFormat(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to prove pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDoc_db_storage(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)

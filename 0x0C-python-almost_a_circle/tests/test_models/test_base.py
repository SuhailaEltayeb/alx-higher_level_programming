#!/usr/bin/python3
"""Base class test module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base class test"""

    def setUp(self):
        """Module import, and class initiation"""
        Base._Base__nb_objects = 0
        pass


    def tearDown(self):
        """After test claen up"""
        pass

    def test_G_id_keyword(self):
        """Keyword arg test"""
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_int(self):
        """custom int id test"""
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_instantiation(self):
        """Base initialization test"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_nb_objects_initializion_0(self):
        """nb_objects initializes to zero test"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_nb_objects_private(self):
        """nb_objects is private class attribute test"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_D_constructor(self):
        """Constructor signature test"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        """Tests consecutive ids test"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    if __name__ == "__main__":
    unittest.main()

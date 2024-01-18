#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Base class test"""

    def setUp(self):
        """Module imprt, class initialization"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """After test cleanup"""
        pass

    def test_inheritance(self):
        """Test square/base inheritence"""
        self.assertTrue(issubclass(Square, Base))

    def test_A_class(self):
        """Square class type test"""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_D_instantiation(self):
        """Class instantiation test"""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

    def test_constructor_noargs(self):
        """Constructor signature test"""
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_manyargs(self):
        """Tests constructor signature test"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments \
                but 6 were given"
        self.assertEqual(str(e.exception), s)

    def test_E_id_inherited(self):
        """Id/base inheritenc test"""
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)


if __name__ == "__main__":
    unittest.main()

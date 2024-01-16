#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    """Base class test"""

    def setUp(self):
        """Module import, and class initialization"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """After test cleanup"""
        pass

    def test_B_inheritance(self):
        """Rest rectangle/ Base inheritence"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_A_class(self):
        """Rectangle class type test"""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_E_id_inherited(self):
        """Id inheritence from Base test"""
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        """property getters/setters test"""
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

    def invalid_types(self):
        """Type validation test"""
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_value_zero(self):
        """Tests property validation test"""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

if __name__ == "__main__":
    unittest.main()

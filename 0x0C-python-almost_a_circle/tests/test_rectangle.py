#!/usr/bin/python3

"""
Defines unnittestsfor models/rectangles.py
    rectangle intstantiation

"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle_instantiation(unittest.TestCase):
    """Unnittests for testing instantiation of class REctangle"""

    def test_rectangle_instance_base(self):
        self.assertIsInstance(Rectangle(10,2),Base)
    
    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()
    def test_only_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
    def test_two_to_four_args(self):
        r1 = Rectangle(5,1)
        r2 = Rectangle(6,2)
        self.assertEqual(r1.id, (r2.id - 1))

    def test_five_args(self):
        r1 = Rectangle(1,2,3,4,5)
        self.assertEqual(r1.id, 5)
    
    def more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1,2,3,4,5,6)
    
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

class Test_Rectangle_width(unittest.TestCase):
    """
    unittests to test the intantiation of width
    """
    def test_no_args(self):
        with self.assertRaisesRegex(TypeError,"width must be an interger"):
            Rectangle(None, 2)
    
    def test_width_isint(self):
        r1 = Rectangle(4,5)
        if self.assertEqual(isinstance(r1.width, int),True):
            return True
        else:
            return "width must be an interger"


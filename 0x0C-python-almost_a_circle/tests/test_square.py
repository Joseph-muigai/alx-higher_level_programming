#!/usr/bin/python3
"""Test cases for the Square class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Square(unittest.TestCase):
    """unitTests for testing the Square class"""

    def setUp(self) -> None:
        """Method invoked for each test"""
        Base._Base__nb_objects = 0
        self.s1 = Square(4)
    
    def test_new_square(self):
        """Test new square """
        self.assertEqual(self.s1.id, 1)
    
    def test_is_Base_instance(self):
        """Check if square is an instance og Base"""
        self.assertEqual(isinstance(self.s1, Base), True)
    
    def test_is_Rectangle_instance(self):
        """Check if Square is an instance of Rectangle"""
        self.assertEqual(isinstance(self.s1, Rectangle),True)
    
    def test_access_to_private_attributes(self):
        """Trying to access privte attributes"""
        with self.assertRaises(AttributeError):
            self.s1.__height
            self.s1.__width
            self.s1.__x
            self.s1.__y
    
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
    
    def test_str(self):
        """Test the __str__method"""
        s1 = Square( 10,11,12,13)
        self.assertEqual(s1.__str__(), "[Square] (13) 11/12 - 10")


    def test_update(self):
        
        """Test update method on Square.
                """

        s1 = Square(8)
        s1.update(30)
        self.assertEqual(s1.id, 30)
    
    def test_to_dictionary(self):
        """Test for public method to_dictionary.
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
"""Module containing the Test cases for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base(unittest.TestCase):
    """unitTests for testing the Base class"""
    def setUp(self):
        """
        method invoked for each test
        """
        Base._Base__nb_objects = 0
    
    def test_id(self):
        """Test the id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
    
    def test_type(self):
        """Test if an object of base is of Type Base"""
        b1 = Base()
        self.assertEqual(type(b1), Base)
        self.assertTrue(isinstance(b1, Base))
    
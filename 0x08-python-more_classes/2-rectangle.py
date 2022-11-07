#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width = 0, height = 0):
        """initalize a new rectangle"""
        self.width = width
        self.height =height

    @property
    def width(self):
        """get the value of the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """get the value of the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__height  == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

#!/usr/bin/python3
"""
Define a  class Rectangle that inherits from class Base
"""

from models.base import Base
class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @ property
    def width(self):
        """
        getter function for width
        """
        return self.__width
    @width.setter
    def width(self,value):
        """
        setter function for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @ property
    def height(self):
        """
        getter function for height
        """
        return self.__height
    @height.setter
    def height(self,value):
        """
        setter function for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    

    @ property
    def x(self):
        """
        getter function for x
        """
        return self.__x
    @x.setter
    def x(self,value):
        """
        setter function for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @ property
    def y(self):
        """
        getter function for y
        """
        return self.__y
    @y.setter
    def y(self,value):
        """
        setter function for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width
    
    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for h in range(self.__height):
            print ("#" * self.__width)
    
    def __str__(self):
        """
        returns an objects representation as a class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
        self.id, 
        self.__x, 
        self.__y,
        self.__width,
        self.__height
        )
#!/usr/bin/python3
"""
Define a  class Rectangle that inherits from class Base
"""
from turtle import width
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
        self.__y = value
    

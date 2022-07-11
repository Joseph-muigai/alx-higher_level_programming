#!/usr/bin/python3
"""
Defines a clsas Square that inherits from rectangle
"""
from rectangle import Rectangle
class Square(Rectangle):
    """
    class square
    """
    def __init__(self,size, x=0, y=0, id=None):
        """
        initalize the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns an objects representation as a string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
            )
    @property
    def size(self):
        """
        getter function for size
        """
        return self.width
    @size.setter
    def size(self,value):
        self.width = value
        self.height = value
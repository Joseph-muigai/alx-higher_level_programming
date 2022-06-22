#!/usr/bin/python3
"""class square thta defines a square"""
class Square:
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
    
    def area(self):
        return self.__size **2


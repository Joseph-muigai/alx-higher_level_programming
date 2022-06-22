#!/usr/bin/python3
"""Represent a square."""
class Square:
    def __init__(self, size=0):
        """
        size - the size of the square 
        """
        if not isinstance(size, int):
            raise TypeError ("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

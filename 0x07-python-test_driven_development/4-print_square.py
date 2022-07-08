#!/usr/bin/python3
"""
Defines a function that prints a square with the character #
"""
def print_square(size):
    """
    a function that prints a square with the character #

    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    
    if size < 0 :
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print('#' * size)

# print_square(4)
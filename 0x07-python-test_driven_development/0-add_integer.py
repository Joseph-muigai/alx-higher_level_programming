#!/usr/bin/python3
"""
Defines a function that adds 2 intergers
"""
def add_integer(a, b=98):
    """
    a funtion that adds 2 intergers
    a and b must be intergers otherwise throw a typeError
    """
    if isinstance(a,int) is False  and isinstance(a,float)is False :
        raise TypeError("a must be an integer")
    if isinstance(b,int) is False and isinstance(b,float)is False :
        raise TypeError("b must be an integer")
    
    return( int(a) + int(b))


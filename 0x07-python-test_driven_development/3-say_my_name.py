#!/usr/bin/python3
"""
Defines a function that prints My name is <first name> <last name>

"""
def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first name> <last name>
    first_name and last_name must be strings otherwise, 
    raise a TypeError exception with the message first_name must be a string or last_name must be a string
    """
    if isinstance(first_name, str)  is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')
    
    print("My name is {} {}".format(first_name, last_name))


# say_my_name("joseph", 7)
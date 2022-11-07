<<<<<<< HEAD
#!/usr/bin/python3
# 2-is_same_class.py
# Gedeon Obae Gekonge <gideonobae@gmail.com>
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
=======
#!/usr/bin/python3
"""
Defines a function that returns True if the object is 
exactly an instance of the specified class
"""
def is_same_class(obj, a_class):
    """
    a function that returns True if the object is 
    exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
>>>>>>> 62368ea1ba978dc845934bd6fe50f77ef9c79c6e

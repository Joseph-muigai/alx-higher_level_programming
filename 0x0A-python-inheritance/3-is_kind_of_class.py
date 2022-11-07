<<<<<<< HEAD
#!/usr/bin/python3
# 3-is_kind_of_class.py
# Gedeon Obae Gekonge <gideonobae@gmail.com>
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
=======
#!/usr/bin/python3
"""
Defines a function that returns True 
if the object is an instance of, or 
if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""
def is_kind_of_class(obj, a_class):
    """
    a function that returns True 
    if the object is an instance of, or 
    if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
>>>>>>> 62368ea1ba978dc845934bd6fe50f77ef9c79c6e

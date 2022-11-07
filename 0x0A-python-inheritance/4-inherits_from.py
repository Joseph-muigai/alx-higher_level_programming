<<<<<<< HEAD
#!/usr/bin/python3
# 4-inherits_from.py
# Gedeon Obae Gekonge <gideonobae@gmail.com>
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
=======
#!/usr/bin/python3
"""
Defines  a function that return True if the object is
an instance of a class that inherited( directly or indirectly)
from the specified class otherwise False
"""
def inherits_from(obj, a_class):
    """
    a function that return True if the object is
    an instance of a class that inherited( directly or indirectly)
    from the specified class otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
        
>>>>>>> 62368ea1ba978dc845934bd6fe50f77ef9c79c6e

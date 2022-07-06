#!/usr/bin/python3
"""
defines a function thta returns the dictinary description
with simple data structure for json serialization of an aobject
"""

def class_to_json(obj):

    """
     returns the dictinary description
    with simple data structure for json serialization of an aobject
    """
    return obj.__dict__

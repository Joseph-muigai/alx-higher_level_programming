#!/usr/bin/python3
"""
Defines a funtion that returns a JSON representation of an object
"""

def to_json_string(my_obj):
    """ returns a JSON representation of an object"""
    import json
    return(json.dumps(my_obj))

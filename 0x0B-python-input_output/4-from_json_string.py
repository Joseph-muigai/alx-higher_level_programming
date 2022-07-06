#!/usr/bin/python3
"""Defines a funtion that returns an object represented in json format"""

def from_json_string(my_str):
    """returns an object represented in json format"""
    import json
    return json.loads(my_str)

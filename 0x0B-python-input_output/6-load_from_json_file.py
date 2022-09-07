#!/usr/bin/python3

"""
Defines a function that creates an object form a json file
"""

def load_from_json_file(filename):
    """ creates an object from a json file"""
    with open( filename, encoding = "utf -8") as f:
        import json
        return json.load(f)

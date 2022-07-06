#!/usr/bin/python3

"""
Defines a function that creates an object form a json file
"""

def load_from_json_file(filename):
    """ creates an object from a json file"""
    with open( filename, encoding = "utf -8") as f:
        txt = f.read(filename)
        import json
        return json.loads(txt)

#!/usr/bin/python3

"""
Defines a functio that writes an objectc to a text file 
using the json representation
"""

def save_to_json_file(my_obj, filename):
    """writes an object to a text file using the json representation"""
    with open(filename, mode="w", encoding = 'utf-8') as f:
        import json
        txt = json.dumps(my_obj)
        f.write(txt)

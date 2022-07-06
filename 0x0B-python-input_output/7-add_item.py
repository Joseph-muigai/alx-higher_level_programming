#!/usr/bin/python3
"""
defines a script that adds all arguments to a Python list, and then save them to a file
"""

from sys import agrv

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json =__import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json(filename)
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json(json_list, filename)

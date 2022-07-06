#!/usr/bin/python3
"""
defines a script that adds all arguments to a Python list, and then save them to a file
"""

import sys

save_to_json = __import__("5-save_to_json_filie").save_to_json_file
load_from_json =__import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json(filename)
except:
    json_list = []
for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])
    save_to_json(json_list, filename)

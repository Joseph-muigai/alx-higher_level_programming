#!/usr/bin/python3
"""Defines a funtion that reads from a file"""

def read_file(filename=""):
    """Prints the contents of the filename"""
    with open(filename, encoding ="utf-8") as f:
        print(f.read(), end = "")

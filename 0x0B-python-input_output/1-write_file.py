#!/usr/bin/python3

"""Defines a funtion that writes a string to a file"""

def write_file(filename="", text=""):

    """writes a string to a text and returns the number of charcters written"""
    with open(filename, mode = 'w', encoding = 'utf-8') as f:
        f.write(text)

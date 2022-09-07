#!/usr/bin/python3

"""Defines a function that appends a string at tthe end od a texte file"""
def append_write(filename="", text=""):
    """ appends a string at the end od a text file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return(f.write(text))

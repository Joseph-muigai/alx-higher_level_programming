#!/usr/bin/python3
"""Defines a class MyList thta inherits class List"""

class MyList(List):
    """imprements sorted printing"""
    def print_sorted(self):
        """Printd a list sorted in ascending order"""
        print(sorted(self))
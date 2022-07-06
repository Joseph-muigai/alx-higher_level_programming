#!/usr/bin/python3

"""defines a class student"""

class Student:
    """
    Public instance attributes:
    first_name
    last_name
    age
    public methods:
    def to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dict[attr] = self.__dict__[attr]
            return dict

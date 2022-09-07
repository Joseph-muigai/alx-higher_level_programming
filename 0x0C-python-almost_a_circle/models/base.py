#!/usr/bin/python3
"""
Defines a class named Base

"""
from fileinput import filename
import json
class Base:
    """
    class Base
    """

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """
        Returns a  json representation of list_dictionaries
        list_dictionaries is a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
       """
       writes the JSON string representation of list_objs to a file
       list_objs is a list of instances who inherits of Base

       """
       fileName = cls.__name__ + ".json"
       with open(fileName, "w") as jsonFile:
        if list_objs is None:
            jsonFile.write("[]")
        else:
            list_dicts = [objs.to_dictionary() for objs in list_objs]
                
            jsonFile.write(Base.to_json_string(list_dicts))
    
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        json_string is a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    @classmethod
    def load_from_file(cls):
        filename =str(cls.__name__)+ '.json'

        try:
            with open(filename, "r", ) as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
        

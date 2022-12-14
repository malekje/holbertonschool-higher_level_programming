#!/usr/bin/python3
"""
base class

"""
import json


class Base:
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string to a file"""
        filename = cls.__name__ + ".json"
        list_dic = []

        if list_objs is None:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list_dic))
            return
        for obj in list_objs:
            list_dic.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON stirng"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

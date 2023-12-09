#!/usr/bin/python3
"""This is the base module"""
from json import dumps, loads
import csv


class Base:
    """This is the cls base where everything is instantiated"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This init method shall initializes the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This rep to json method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This rep the save to file method
        Args:
           cls: represent the class
           list_objs: rep the list objects
        Returns:
           None
        """
        filename = cls.__name__ + ".json"
        nuevo_lst = []
        if list_objs is not None:
            for x in list_objs:
                nuevo_lst.append(cls.to_dictionary(x))
        with open(filename, "w") as y:
            y.write(cls.to_json_string(nuevo_lst))

    @staticmethod
    def from_json_string(json_string):
        """This represent the from json method"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """This shall represent the create method
        Args:
            cls: this rep class
            **dictionary:this rep dict
        Returns:
            dummy
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """This shall return a list of inst"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as y:
                nuevo_lst = cls.from_json_string(y.read())
                for x in range(len(nuevo_lst)):
                    nuevo_lst[x] = cls.create(**nuevo_lst[x])
                return nuevo_lst
        except FileNotFoundError:
            return ([])
        except Exception as e:
            print("An error occurred while loading from file:", str(e))
            return ([])

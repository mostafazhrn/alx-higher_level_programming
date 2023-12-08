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

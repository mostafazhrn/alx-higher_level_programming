#!/usr/bin/python3
"""This is module for student class"""


class Student:
    """This is student class"""

    def __init__(self, first_name, last_name, age):
        """This init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """THis instance retrieve dict representation of class"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            if x in self.__dict__:
                new_dict[x] = self.__dict__[x]
        return new_dict

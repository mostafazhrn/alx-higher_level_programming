#!/usr/bin/python3
"""This is module for student class"""


class Student:
    """This is student class"""

    def __init__(self, first_name, last_name, age):
        """This init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """THis instance retrieve dic representation"""

        return self.__dict__

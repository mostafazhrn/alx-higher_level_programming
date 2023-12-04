#!/usr/bin/python3
"""This is module of rectangle class ex of inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is the rec sub class"""

    def __init__(self, width, height):
        """This is the init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This shall calcuale area of W and H"""
        return self.__width * self.__height

    def __str__(self):
        """This represent the print method"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

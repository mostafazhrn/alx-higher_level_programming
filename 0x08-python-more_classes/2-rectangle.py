#!/usr/bin/python3
"""This module defines a rectangle
based on the previous script
"""


class Rectangle:
    """This class have private instance.
    it shall take two argument width& height.
    """
    def __init__(self, width=0, height=0):
        """Starting instance of optional widthand height"""

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """This is the def height(self): to retrieve height"""

        return self.__height

    @height.setter
    def height(self, value):
        """This set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @property
    def width(self):
        """This is the def width(self) instance: to retrieve width"""

        return self.__width

    @width.setter
    def width(self, value):
        """def width(self, value): to set it"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    def area(self):
        """This shall return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """This shall returns rectangle parmeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

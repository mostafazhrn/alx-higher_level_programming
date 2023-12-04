#!/usr/bin/python3
"""This is square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class inherit from Rec"""

    def __init__(self, size):
        """This is init method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This func calc area of sq"""
        return (self.__size ** 2)

    def __str__(self):
        """This shall print the desciption of sq"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

#!/usr/bin/python3
"""this code define class Square"""


class Square:
    """ this start class square"""
    def __init__(self, size=0):
        """this shall start the size"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        """method define square area"""
    def area(self):
        """it shall return square area"""
        return self.__size**2

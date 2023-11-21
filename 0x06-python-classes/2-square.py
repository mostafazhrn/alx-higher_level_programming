#!/usr/bin/python3
"""this code define class square with priv attribute size"""


class Square:
    """this defines class"""
    def __init__(self, size=0):
        """this starts class"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

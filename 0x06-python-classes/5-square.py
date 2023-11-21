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
    """public instance def size (self)"""
    @property
    def size(self):
        """to get it back"""
        return self.__size
    """public instance def size(self,value):"""
    @size.setter
    def size(self, value):
        """ this shall set it up"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    """public instance def my_print(self):"""
    def my_print(self):
        """it shall print square with char to stdout"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)

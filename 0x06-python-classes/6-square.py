#!/use/bin/python3
"""This code define class Square to do square generation module."""


class Square:
    """ This start class square with its attributes.
    size (int), position (tuple), __size."""
    def __init__(self, size=0, position=(0, 0)):
        #This shall start the size and position.
        self.__size = size
        self.__position = position
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        if type(self.__position) is not tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) is not int or self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[1]) is not int or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        """Public instance method: shall define square area."""
    def area(self):
        """it shall return square area"""
        return self.__size**2
    """Public instance method: def size (self):."""
    @property
    def size(self):
        """to get it back"""
        return self.__size
    """public instance method: def size(self,value):."""
    @size.setter
    def size(self, value):
        """ this shall set it up"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    """Public instance method: def position(self):."""
    @property
    def position(self):
        """to retrieve it"""
        return self.__position
    """Public instance method: def position(self, value):."""
    @position.setter
    def position(self, value):
        """to set it"""
        self.__position = value
        if type(self.__position) is not tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) is not int or self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[1]) is not int or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
    """Public instance method: of def my_print(self):."""
    def my_print(self):
        """it shall print square with char to stdout."""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#"
                                    * self.__size))

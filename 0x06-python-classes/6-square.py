#!/use/bin/python3
"""This module defines the Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is
            not a tuple of 2 positive integers.
            ValueError: If size is less than 0.

        Returns:
            None
        """
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

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        self.__position = value
        if type(self.__position) is not tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) is not int or self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[1]) is not int or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print the square to stdout.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#"
                                    * self.__size))

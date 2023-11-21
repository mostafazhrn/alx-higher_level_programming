#!/use/bin/python3
"""this code define class Square"""


class Square:
    """This start class square"""
    def __init__(self, size=0, position=(0, 0)):
        """This shall start the size and position.

        Args:
            size (int): the first parameter
            position (tuple): the second parameter
        Returns:
            It shall return squared area.
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

        """method define square area"""
    def area(self):
        """It shall return square area

        Attributes:
              __size (int): len of square side

        
        Returns:
               _area square area
        """
        return self.__size**2
    
    """public instance def size (self)"""

    @property
    def size(self):
        """Getter to get it back.

        Returns:
               size (int): len squared of side.
        """
        return self.__size
    
    """public instance def size(self,value):"""
    @size.setter
    def size(self, value):
        """ Args: this shall set it up.

        value (int): len of side of square

        Attributes:
                 __size (int): len of side of square


        Raises:
            ValueError: if value < 0
            TypeError: of value is not int.

        
        """
        
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        
    """Public instance method: def position(self):"""
    
    @property
    def position(self):
        """Getter to retrieve the position.


        Returns:
             __position (tuple): horizontal and vertical offset
        
        """
        return self.__position
            
    """Public instance method: def position(self, value):"""
    @position.setter
    def position(self, value):
        """This shall set it.


        Args:
          value (int): shall take two int


        Attributes:
           __position (tuple): horizontal and veritcal offset of sqaure


        Raises:
            TypeError: 3 errors if value not tuple

        
        """
        self.__position = value
        if type(self.__position) is not tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[0]) is not int or self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(self.__position[1]) is not int or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
    """public instance of def my_print(self):"""
    def my_print(self):
        """It shall print square with char to stdout.


        Attributes:
             __size (int): len of square side
             __position (tuple): shall represent the veritcal and
             horizontal offset of square


        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#"
                                    * self.__size))

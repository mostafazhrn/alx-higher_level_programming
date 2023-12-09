#!/usr/bin/python3
"""This is the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """This is the rec class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This shall be getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this shall be the setter methd"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """This shall be getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """this hsall be the setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """This shall be getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """this hsall be the setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """This is the area method that defines the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """THis shall represent the display method"""
        for x in range(self.__y):
            print("")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """THis represent the str method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """This represent update method
        Args:
            *args: arguments
            **kwargs: keyword arguments
        Returns:
            None
        """
        if args is not None and len(args) != 0:
            for x in range(len(args)):
                if x == 0:
                    self.id = args[x]
                if x == 1:
                    self.width = args[x]
                if x == 2:
                    self.height = args[x]
                if x == 3:
                    self.x = args[x]
                if x == 4:
                    self.y = args[x]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.__height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """This rep the dict method"""
        return ({"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y})

#!/usr/bin/python3
"""This module defines a rectangle
based on the previous script
"""


class Rectangle:
    """This class have private instance.
    it shall take two argument width& height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Starting instance of optional widthand height.
        public class Num of instances, init to zero
        """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ This shall Returns a representation of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        row = "{}".format(self.print_symbol) * self.__width
        rect = row
        for i in range(self.__height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """ This Returns a representation of the rec for reproduction """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This shall Print msg when a rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This shall return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        elif rect_2.area() == rect_1.area():
            return rect_1
        else:
            return rect_1

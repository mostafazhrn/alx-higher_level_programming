#!/usr/bin/python3
"""THis represent the module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is sq class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This rep init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This shall rep str method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """This represent the size getter shall get & retrn size"""
        return self.width

    @size.setter
    def size(self, value):
        """This shall represent size setter"""
        self.width = value
        self.height = value

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
                    self.size = args[x]
                if x == 2:
                    self.x = args[x]
                if x == 3:
                    self.y = args[x]
        elif kwargs is not None and len(kwargs) != 0:
            for x in kwargs:
                if x == "id":
                    self.id = kwargs[x]
                if x == "size":
                    self.size = kwargs[x]
                if x == "x":
                    self.x = kwargs[x]
                if x == "y":
                    self.y = kwargs[x]

    def to_dictionary(self):
        """This rep the dict method"""
        return ({"id": self.id, "size": self.size, "x": self.x, "y": self.y})

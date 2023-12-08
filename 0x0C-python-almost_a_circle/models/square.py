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

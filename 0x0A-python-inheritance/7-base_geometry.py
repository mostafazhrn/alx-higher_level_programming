#!/usr/bin/python3
"""This module is class baseGeomtry"""


class BaseGeometry:
    """This class is baseGeometry"""

    def area(self):
        """This func raise instance area not iplemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This func checks value and raise type and val errors
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

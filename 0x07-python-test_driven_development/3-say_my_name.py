#!/usr/bin/python3
"""
This module prints a name
Raises:
TypeError: if first_name or last_name are not strings
"""


def say_my_name(first_name, last_name=""):
    """Prints a name
    Args:
        first_name
        last_name
    Returns:

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""This module return true if instance or false if false if not"""


def is_kind_of_class(obj, a_class):
    """This function check if object if object is from class of not
    Args:
        obj: this represent object arg
        a_class: this represent the class
    Return:
        It shall return true or false
    """
    return isinstance(obj, a_class)

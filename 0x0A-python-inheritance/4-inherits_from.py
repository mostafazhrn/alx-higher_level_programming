#!/usr/bin/python3
"""This module shall return true if class is inhertied and false if not"""


def inherits_from(obj, a_class):
    """This function shall check if class inhertid or not
    Args:
        obj: this represent object
        a_class: this represent class
    Return:
        it shall retrun true or false
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False

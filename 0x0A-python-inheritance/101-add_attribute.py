#!/usr/bin/python3
"""This module add new attr if possible"""


def add_attribute(ob, nom, val):
    """This Func add attribute
    Args:
       ob: this represent the object
       nom: this represent name of attr
       val: this represent valu of the attr
    Returns:
       New attr if possible
    """
    if hasattr(ob, "__dict__"):
        setattr(ob, nom, val)
    else:
        raise TypeError("can't add new attribute")

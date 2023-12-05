#!/usr/bin/python3
"""This module writes str to text and return num of chars"""


def write_file(filename="", text=""):
    """This writes str to text and return num of chars"""

    with open(filename, mode="w", encoding="utf-8") as x:
        return x.write(text)

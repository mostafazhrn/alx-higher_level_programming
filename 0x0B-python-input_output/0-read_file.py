#!/usr/bin/python3
"""This module reads text file encoding UTF-8"""


def read_file(filename=""):
    """This func reads open txt file"""

    with open(filename, encoding="utf-8") as x:
        print(x.read(), end="")

#!/usr/bin/python3
"""THis module append str to txt file"""


def append_write(filename="", text=""):
    """Thisfunc append str to txt and return num of charsadded"""

    with open(filename, mode="a", encoding="utf-8") as x:
        return x.write(text)

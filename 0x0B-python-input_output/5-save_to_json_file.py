#!/usr/bin/python3
"""This module write obj to file txt"""


import json


def save_to_json_file(my_obj, filename):
    """This func write obj to text file"""

    with open(filename, mode="w", encoding="utf-8") as x:
        json.dump(my_obj, x)

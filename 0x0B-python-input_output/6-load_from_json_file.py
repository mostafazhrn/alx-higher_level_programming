#!/usr/bin/python3
"""This module create obj from json file"""


import json


def load_from_json_file(filename):
    """This func create obj from json file"""

    with open(filename, encoding="utf-8")as x:
        return json.load(x)

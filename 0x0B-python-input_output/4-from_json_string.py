#!/usr/bin/python3
"""This module return obj rep by json"""


import json


def from_json_string(my_str):
    """This func return obj represent by json"""

    return json.loads(my_str)

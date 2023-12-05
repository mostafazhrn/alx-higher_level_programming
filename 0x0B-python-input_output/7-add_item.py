#!/usr/bin/python3
"""This module add all args to a python list then to file"""


import sys
import os.path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
json_list = []

if os.path.isfile(filename):
    json_list = load_from_json_file(filename)

for x in range(1, len(sys.argv)):
    json_list.append(sys.argv[x])

save_to_json_file(json_list, filename)

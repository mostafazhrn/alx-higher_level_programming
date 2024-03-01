#!/usr/bin/python3
"""This script shall take URL and send req then display response"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    cod = req.status_code
    if cod >= 400:
        print("Error code: {}".format(cod))
    else:
        print(req.text)

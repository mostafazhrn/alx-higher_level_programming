#!/usr/bin/python3
"""THis script shall take URL and disp value of vriable"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))

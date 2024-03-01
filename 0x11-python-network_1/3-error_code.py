#!/usr/bin/python3
""" THis script shall take URL and send req and display response"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as x:
        print("Error code: {}".format(x.code))

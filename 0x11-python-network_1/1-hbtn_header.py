#!/usr/bin/python3
""" THis script shall take URL and display valu of x request id"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers.get("X-Request-Id"))

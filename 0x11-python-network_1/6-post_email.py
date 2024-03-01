#!/usr/bin/python3
"""THis script shall take URL and email and send POST then disp resp"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={"email": email})
    print(req.text)

#!/usr/bin/python3
"""THis script shall take github cred and use github API to display id"""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get("https://api.github.com/user", auth=(usr, passwd))
    print(req.json().get("id"))

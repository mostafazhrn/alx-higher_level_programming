#!/usr/bin/python3
""" This script shall fetch https://alx-intranet.hbtn.io/status """

import urllib.request
import urllib.parse


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        link = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(link)))
        print("\t- content: {}".format(link))
        print("\t- utf8 content: {}".format(link.decode("utf-8")))

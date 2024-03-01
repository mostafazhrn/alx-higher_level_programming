#!/usr/bin/python3
"""this script shall take letter and send POST req with letter as param"""
import requests
import sys


if __name__ == "__main__":
    x = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        req = requests.post("http://0.0.0.0:5000/search_user",
                            data={"q": x}).json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req.get("id"), req.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

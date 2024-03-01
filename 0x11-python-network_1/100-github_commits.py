#!/usr/bin/python3
"""THis script shall take 2 args to get last 10 commits of a repo """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(owner, repo))
    for x in req.json()[:10]:
        print("{}: {}".format(x.get("sha"), x.get("commit")
                              .get("author").get("name")))

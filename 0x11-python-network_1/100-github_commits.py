#!/usr/bin/python3
'''
Script to list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
'''
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for c in range(10):
            print("{}: {}".format(
                commits[c].get("sha"),
                commits[c].get("commit").get("author").get("name")))
    except IndexError:
        pass

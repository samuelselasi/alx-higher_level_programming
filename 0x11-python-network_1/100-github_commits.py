#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve the challenge"""
from sys import argv
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    fetch_url = requests.get(u)
    commits = fetch_url.json()

    try:
        for commit in range(10):
            print("{}: {}".format(
                commits[commit].get("sha"),
                commits[commit].get("commit").get("author").get("name")))
    except IndexError:
        pass

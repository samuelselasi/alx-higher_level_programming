#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if requests.get(argv[1]).status_code >= 400:
        print("Error code: {}".format(requests.get(argv[1]).status_code))
    else:
        print(requests.get(argv[1]).text)

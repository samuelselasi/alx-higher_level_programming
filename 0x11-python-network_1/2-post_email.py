#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]}).encode("ascii")
    fetch_url = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(fetch_url) as response:
        print(response.read().decode("utf-8"))

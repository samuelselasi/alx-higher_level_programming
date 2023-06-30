#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    fetch_url = requests.post(argv[1], {'email': argv[2]})
    print(fetch_url.text)

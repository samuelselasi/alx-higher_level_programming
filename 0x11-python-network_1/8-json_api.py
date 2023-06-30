#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    url = requests.post("http://0.0.0.0:5000/search_user", {'q': letter})

    try:
        response = url.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))

    except ValueError:
        print("Not a valid JSON")

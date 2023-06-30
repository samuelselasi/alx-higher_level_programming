#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    fetch_url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(fetch_url.text)))
    print("\t- content: {}".format(fetch_url.text))

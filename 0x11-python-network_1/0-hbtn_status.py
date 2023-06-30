#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    fetch_url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(fetch_url) as response:
        output = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(output)))
        print("\t- content: {}".format(output))
        print("\t- utf8 content: {}".format(output.decode("utf-8")))

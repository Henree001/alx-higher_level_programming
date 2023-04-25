#!/usr/bin/python3
import urllib.request
from sys import argv
import urllib.error
""" takes in a URL and, sends a request to the passed URL
and displays the body of the response"""
if __name__ == "__main__":
    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as response:
            rep = response.read()
            print(rep)
    except urllib.error.HTTPError as e:
        print(e.code)

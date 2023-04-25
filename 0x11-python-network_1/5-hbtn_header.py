#!/usr/bin/python3
import requests
from sys import argv
"""takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""
if __name__ == "__main__":
    r = requests.get(argv[1])
    r = r.headers
    print(r['X-Request-Id'])

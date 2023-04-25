#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv
""" takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode()
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        rep = response.read()
        print(rep.decode())

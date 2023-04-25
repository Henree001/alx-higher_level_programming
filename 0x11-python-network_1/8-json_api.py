#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        r = requests.post(url, data={'q': ""})
    else:
        r = requests.post(url, data={'q': argv[1]})
    try:
        r = r.json()
        if not r:
            print('No result')
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except ValueError:
        print('Not a valid JSON')

#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        r = requests.post(argv[1], data={'q': ""})
    else:
        r = requests.get(argv[1], data={'q': argv[2]})
    try:
        r = r.json()
        if len(r) == 0:
            print('No result')
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

#!/usr/bin/python3
import requests
"""Takes URL and prints out response"""
if __name__ == "__main__":
    rep = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(rep)))
    print("\t- content: {}".format(rep.text))

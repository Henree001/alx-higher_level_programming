#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer  ' + argv[2],
               'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=headers)
    r = r.json()
    print(r.get('id'))

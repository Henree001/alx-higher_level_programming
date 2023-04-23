#!/bin/bash
# send a post request with two headers
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

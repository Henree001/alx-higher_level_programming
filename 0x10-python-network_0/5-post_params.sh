#!/bin/bash
# send a post request with two headers
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

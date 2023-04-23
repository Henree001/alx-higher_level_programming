#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep Allow: | cut -b 8-100

#!/bin/bash
# sets a header var with a value of 98
curl -sX GET -H "X-School-User-Id: 98" "$1"

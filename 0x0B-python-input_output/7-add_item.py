#!/usr/bin/python3
"""Add all arguments to a Python list and saves it to a file."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    item = []

items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")

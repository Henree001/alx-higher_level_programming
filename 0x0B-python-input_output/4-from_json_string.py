#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str = json string
    """
    return json.loads(my_str)

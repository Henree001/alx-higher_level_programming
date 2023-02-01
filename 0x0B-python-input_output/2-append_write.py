#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    Args:
        filename: file to be appended
        text: string to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Defines a text file writing function."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of
    characters writtenwrites a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename: file to be written into
        text: string to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

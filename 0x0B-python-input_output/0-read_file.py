#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file to be opened
    """
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read, end='')

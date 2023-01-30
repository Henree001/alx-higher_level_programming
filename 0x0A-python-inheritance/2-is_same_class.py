#!/usr/bin/python3
"""Defines a module."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
    class; otherwise False.
    Args:
        0bj: the object to check
        a_class: The class to match the type of obj to.
    """

    if type(obj) == a_class:
        return True
    return False

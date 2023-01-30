#!/usr/bin/python3
"""Defines a module"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    """
    if isinstance(obj, a_class):
        return True
    return False

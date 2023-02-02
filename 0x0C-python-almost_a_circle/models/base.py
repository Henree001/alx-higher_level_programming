#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """Represents a base model class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize class attributes
        args:
            id: integer
        """
        if id not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

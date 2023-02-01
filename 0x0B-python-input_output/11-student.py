#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if type(attrs) == list and all(type(item) == str for item in attrs):
            my_dict = {}
            for items in attrs:
                if hasattr(self, items):
                    my_dict[items] = getattr(self, items)
                    return my_dict
        return vars(self)

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance
        Args:
            json: a dictionary that contains the new attributes
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

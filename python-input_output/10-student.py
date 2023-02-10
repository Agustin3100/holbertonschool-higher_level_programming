#!/usr/bin/python3
"""Holberton School."""


class Student:
    """My class."""

    def __init__(self, first_name, last_name, age):
        """My class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """My class."""
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        else:
            return self.__dict__

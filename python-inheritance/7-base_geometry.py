#!/usr/bin/python3
"""Holberton School."""


class BaseGeometry:
    """Class for example."""

    pass

    def area(self):
        """Class for example."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Class for example."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

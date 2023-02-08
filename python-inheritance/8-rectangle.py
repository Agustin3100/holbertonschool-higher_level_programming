#!/usr/bin/python3
"""Holberton School."""
#  BaseGeometry = __import__('7-base_geometry').BaseGeometry


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


class Rectangle(BaseGeometry):
    """Class for example."""

    def __init__(self, width, height):
        """Init for example."""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

#!/usr/bin/python3
"""Holberton School."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for example."""

    def __init__(self, width, height):
        """Init for example."""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

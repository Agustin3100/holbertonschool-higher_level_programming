#!/usr/bin/python3
"""Holberton School."""


class Rectangle:
    """Class that prints a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Function."""
        Rectangle.rectangle = {}
        self.__height__ = height
        self.__width__ = width

    @property
    def width(self):
        """Returns width variable."""
        return self.__width__

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if self.__width__ < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """Returns width variable."""
        return self.__height__

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if self.__height__ < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value

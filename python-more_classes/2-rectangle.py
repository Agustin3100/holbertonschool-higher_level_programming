#!/usr/bin/python3
"""Holberton School."""


class Rectangle:
    """Class that prints a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Function."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

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

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print rectangle description."""
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """Class for example."""

    def __init__(self, size):
        """Return size."""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Return area of rectangle."""
        return self.__size ** 2

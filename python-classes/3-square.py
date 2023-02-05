#!/usr/bin/python3
"""Holberton School."""


class Square:
    """Square class."""

    def __init__(self, __size__=0):
        """Asign size to the square with ifs."""
        if int(__size__) < 0:
            raise ValueError("size must be >= 0")
        elif type(__size__) != int:
            raise TypeError("size must be an integer")
        self.__size__ = __size__

    def area(self):
        """Return area of the square."""
        return int(self.__size__ ** 2)

#!/usr/bin/python3
"""Holberton School."""


class Square:
    """Square class."""

    def __init__(self, __size__=0, __position=(0, 0)):
        """First instance."""
        if int(__size__) < 0:
            raise ValueError("size must be >= 0")
        elif type(__size__) != int:
            raise TypeError("size must be an integer")
        self.__size__ = __size__

    def area(self):
        """Return area of the square."""
        return int(self.__size__ ** 2)

    @property
    def position(self):
        """Return position."""
        return self.position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    @property
    def size(self):
        """Return size."""
        return self.__size__

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size__ = value

    def my_print(self):
        """Print hash."""
        if self.__size__ != 0:
            for i in range(self.__size__):
                print('#' * self.__size__)
        else:
            print()
        if self.position[1] > 0:
            for i in range(self.position):
                print(" " * self.position)

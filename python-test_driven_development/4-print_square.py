#!/usr/bin/python3
"""Holberton School."""


def print_square(size):
    """Print a square."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size != 0:
        for i in range(size):
            print('#' * size)

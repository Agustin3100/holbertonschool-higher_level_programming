#!/usr/bin/python3
"""Holberton School."""


def add_integer(a, b=98):
    """Add an integer."""
    if not isinstance((a), (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance((b), (int, float)):
        raise TypeError("b must be an integer")
    return a + b

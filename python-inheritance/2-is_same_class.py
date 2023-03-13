#!/usr/bin/python3
"""Holberton School."""


def is_same_class(obj, a_class):
    """Check if object is an instance of a_class."""
    if type(obj) is a_class:
        return True
    else:
        return False

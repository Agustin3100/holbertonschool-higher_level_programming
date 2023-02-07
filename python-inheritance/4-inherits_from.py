#!/usr/bin/python3
"""Holberton School."""


def inherits_from(obj, a_class):
    """Check for inherits and subclasses."""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)

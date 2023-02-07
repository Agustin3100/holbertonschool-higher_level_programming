#!/usr/bin/python3
"""Holberton School."""


def is_kind_of_class(obj, a_class):
    """Check if the obj is an instance of a_class and if its inherited from."""
    if isinstance(obj, a_class):
        return True
    else:
        return False

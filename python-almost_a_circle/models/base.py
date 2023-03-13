#!/usr/bin/python3
"""Holberton School."""


class Base:
    """Class for example."""

    _nb_objects = 0

    def __init__(self, id=None):
        """Func for example."""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

#!/usr/bin/python3
"""Holberton School."""


def write_file(filename="", text=""):
    """Write and return characters written."""
    if not filename:
        raise ValueError('Cannot convert empty string')
    with open(filename, 'r+') as f:
        f.read()
        f.seek(0)
        f.write(text)
        f.truncate()
    return len(text)

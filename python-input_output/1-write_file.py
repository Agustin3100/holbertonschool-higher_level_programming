#!/usr/bin/python3
"""Holberton School."""


def write_file(filename="", text=""):
    """Write and return characters written."""
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(text)
        return len(text)

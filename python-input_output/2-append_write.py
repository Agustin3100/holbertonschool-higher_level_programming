#!/usr/bin/python3
"""Holberton School."""


def append_write(filename="", text=""):
    """Write and return characters written."""
    with open(filename, "a", encoding="utf-8") as fp:
        fp.write(text)
        return len(text)

#!/usr/bin/python3
"""Holberton School."""


def read_file(filename=""):
    """Read and print file."""
    if not filename:
        raise ValueError('Cannot convert empty string')
    with open(filename, 'r') as f:
        print(f.read())
    f.closed

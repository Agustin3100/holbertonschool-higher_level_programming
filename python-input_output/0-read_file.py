#!/usr/bin/python3
"""Holberton School."""


def read_file(filename=""):
    """Read and print file."""
    with open(filename, 'r') as f:
        print(f.read())

#!/usr/bin/python3
"""Holberton School."""


read_file = __import__('0-read_file.py').read_file


def class_to_json(obj):
    """My class."""
    return {"name": obj.name, "number": obj.number}

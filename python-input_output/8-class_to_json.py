#!/usr/bin/python3
"""Holberton School."""


import json
read_file = __import__('0-read_file.py').read_file


def class_to_json(obj):
    """My class."""
    read_file(obj)
    json.dumps(obj)

#!/usr/bin/python3
"""Holberton School."""


import json


def load_from_json_file(filename):
    """Return obj represetation of json."""
    with open(filename, "w", encoding="utf-8") as fp:
        obj = fp.read()
        return json.loads(obj)

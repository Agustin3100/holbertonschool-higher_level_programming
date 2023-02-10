#!/usr/bin/python3
"""Holberton School."""


import json


def save_to_json_file(my_obj, filename):
    """Return obj represetation of json."""
    with open(filename, "w", encoding="utf-8") as fp:
        cnvrtd = json.dumps(my_obj)
        fp.write(cnvrtd)

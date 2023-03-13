#!/usr/bin/python3
"""Holberton School."""


def text_indentation(text):
    """Indents text."""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(0, len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
        elif text[i] == " ":
            for j in range(i, 0, -1):
                if text[j] == " ":
                    continue
                elif text[j] in [".", "?", ":"]:
                    break
                else:
                    print(text[i], end="")
                    break
        else:
            print(text[i], end="")

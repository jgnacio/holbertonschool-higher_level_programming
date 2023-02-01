#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 1 09:48:00 2023.

@author: jgnacio
@description:
This module have a function:
    text_indentation (text) - that prints
    print the indentation but replace all characters
    after . ? and : with new lines.
"""


def text_indentation(text):
    """Print the indentation of the given text indented after . ? and : ."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    matches = [".", "?", "."]
    index = 0
    while index < len(text):
        if text[index] in matches:
            print(f"{text[index]}\n\n", end="")
            try:
                if text[index + 1] == " ":
                    index += 2
                else:
                    index += 1
            except IndexError:
                pass
        else:
            print(text[index], end="")
            index += 1

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 1 09:48:00 2023.

@author: jgnacio
@description:
This module have a function:
    text_indentation (text) - that prints
    the size of the square
"""


def text_indentation(text):
    """Print the indentation of the given text separated by . ? and : ."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = text.replace(". ", "\n\n").replace("? ", "\n\n").replace(": ", "\n\n")
    print(s)

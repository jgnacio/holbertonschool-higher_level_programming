#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 15:18:00 2023.

@author: jgnacio
@description:

"""


def append_write(filename="", text=""):
    """Write a file."""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)

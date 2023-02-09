#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 15:18:00 2023.

@author: jgnacio
@description:

"""


def write_file(filename="", text=""):
    """Write a file."""
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)

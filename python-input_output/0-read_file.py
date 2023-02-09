#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 15:18:00 2023.

@author: jgnacio
@description:

"""


def read_file(filename=""):
    """Read a file."""
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read())

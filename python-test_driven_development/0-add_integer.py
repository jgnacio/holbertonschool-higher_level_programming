#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:08:00 2023.

@author: jgnacio
@description:
This module have a function:
    add_integer (int, int) - that add two integers
"""


def add_integer(a, b=98):
    """Add two integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

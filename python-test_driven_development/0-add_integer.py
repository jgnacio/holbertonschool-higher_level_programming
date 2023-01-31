#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:08:00 2023.

@author: jgnacio
@description:
This module have a function:
    add_integer (int, int) - that add two integers
"""


def add_integer(a=None, b=None):
    """Add two integers."""
    if not isinstance(a, int):
        print("a must be an integer")
        return
    if not isinstance(b, int):
        print("b must be an integer")
        return
    return a + b

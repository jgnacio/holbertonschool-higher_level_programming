#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 1 09:48:00 2023.

@author: jgnacio
@description:
This module have a function:
    print_square (size) - that prints
    the size of the square
"""


def print_square(size):
    """Print the square."""
    if (not isinstance(size, int) or
       (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:15:00 2023.

@author: jgnacio
@description:

"""


def pascal_triangle(n):
    """Calculate the nth Pascal triangle."""
    row = []
    for num in range(n):
        x = 11**num
        row.append(str(x))
    return row

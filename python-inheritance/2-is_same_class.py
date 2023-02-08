#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 12:13:00 2023.

@author: jgnacio
@description:

"""


def is_same_class(obj, a_class):
    """Retrun if obj is instance of a class."""
    if type(obj) is a_class:
        return True
    return False

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 12:13:00 2023.

@author: jgnacio
@description:

"""


def inherits_from(obj, a_class):
    """Function that verify that a class inherits from a given class."""
    if type(obj) is a_class:
        return False

    return issubclass(a_class, type(obj))

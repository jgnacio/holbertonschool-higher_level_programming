#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 12:13:00 2023.

@author: jgnacio
@description:

"""


def is_kind_of_class(obj, a_class):
    """Return if obj is instance of a class."""
    if isinstance(obj, a_class):
        return True
    return False

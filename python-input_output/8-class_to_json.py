#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:29:00 2023.

@author: jgnacio
@description:

"""


def class_to_json(obj):
    """Return JSON string from object class."""
    return obj.__dict__

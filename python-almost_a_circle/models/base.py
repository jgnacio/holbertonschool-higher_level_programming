#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:46:00 2023.

@author: jgnacio
@description:

"""


class Base:
    """Represents a base class object."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

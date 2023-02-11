#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:45:00 2023.

@author: jgnacio
@description:

"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Create a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a json representation of this student."""
        return self.__dict__

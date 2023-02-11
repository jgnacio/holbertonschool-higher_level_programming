#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:10:00 2023.

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

    def to_json(self, attrs=None):
        """Return a json representation of this student."""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for elem in attrs:
            if elem in self.__dict__.keys():
                new_dict[elem] = self.__dict__[elem]
        return new_dict

    def reload_from_json(self, json):
        """Reload attributes of the student."""
        for key, value in json.items():
            setattr(self, key, value)

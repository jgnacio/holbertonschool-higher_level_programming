#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:46:00 2023.

@author: jgnacio
@description:

"""

import json


class Base:
    """Represents a base class object."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a json string."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file."""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(file_name, "w", encoding="UTF-8") as file:
            file.write(Base.to_json_string(new_list))

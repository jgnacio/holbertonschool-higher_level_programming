#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:09:00 2023.

@author: jgnacio
@description:

"""

import json


def load_from_json_file(filename):
    """Return a object from a JSON file."""
    with open(filename, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:46:00 2023.

@author: jgnacio
@description:

"""

import json


def to_json_string(my_obj):
    """Return a json string representation of an object."""
    return json.dumps(my_obj)

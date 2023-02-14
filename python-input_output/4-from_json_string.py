#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:46:00 2023.

@author: jgnacio
@description:

"""

import json


def from_json_string(my_str):
    """Return a object from a JSON string."""
    return json.loads(my_str)

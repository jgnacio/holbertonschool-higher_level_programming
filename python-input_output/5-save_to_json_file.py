#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:02:00 2023.

@author: jgnacio
@description:

"""

import json


def save_to_json_file(my_obj, filename):
    """Return a object from a JSON string."""
    with open(filename, 'w') as outfile:
        outfile.write(json.dumps(my_obj))

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:27:00 2023.

@author: jgnacio
@description:

"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

with open("add_item.json", "a") as f:
    f.write(str(sys.argv))

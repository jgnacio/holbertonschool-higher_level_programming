#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:36:00 2023.

@author: jgnacio
@description:

"""

import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    jsonobj = load_from_json_file('add_item.json')
except Exception:
    jsonobj = []

for arg in sys.argv[1:]:
    jsonobj.append(arg)

save_to_json_file(jsonobj, "add_item.json")

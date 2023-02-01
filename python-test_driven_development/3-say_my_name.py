#/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 1 09:01:00 2023.

@author: jgnacio
@description:
This module have a function:
    say_my_name (first_name, last_name="") - that prints
    the name of the person
"""


def say_my_name(first_name, last_name=""):
    """Prints the name of the person"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

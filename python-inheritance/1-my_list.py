#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 10:35:00 2023.

@author: jgnacio
@description:

"""


class MyList(list):
    """Print a list in order."""

    def print_sorted(self):
        if hasattr(self, '__str__'):
            print(sorted(self))
            return sorted(self)

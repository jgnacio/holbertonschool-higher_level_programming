#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 12:14:00 2023.

@author: jgnacio
@description:

"""


class BaseGeometry:
    """Base empty class."""

    def area(self):
        """Return the area not implemented."""
        raise Exception("area() is not implemented")

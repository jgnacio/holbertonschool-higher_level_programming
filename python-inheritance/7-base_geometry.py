#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 15:41:00 2023.

@author: jgnacio
"""


class BaseGeometry:
    """Base empty class."""

    def area(self):
        """Return the area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verify that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

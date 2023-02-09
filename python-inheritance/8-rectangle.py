#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wen Feb 8 15:41:00 2023.

@author: jgnacio
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

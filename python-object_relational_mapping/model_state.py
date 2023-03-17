#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 11:29:00 2023.

@author: jgnacio
@description:
    This module if for declaration of
    State class that have this columns:
        (id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(128) NOT NULL)
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class for referencing a table with this caracteristics."""

    __tablename__ = "states"
    id = Column(Integer, autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 14:11:00 2023.

@author: jgnacio
@description:
    This module if for declaration of
    City class that have this columns:
        (id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(128) NOT NULL,
         state_id INT FOREING KEY (state.id))
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """State class for referencing a table with this caracteristics."""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement="auto", primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))

    def __init__(self, name):
        self.name = name

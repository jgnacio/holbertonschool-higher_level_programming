#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 12:22:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy and lists all State
    objects from the database given.
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]),
    pool_pre_ping=True
)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)

session = Session()

states = session.query(State)
for state in states:
    print(f"{state.id}: {state.name}")

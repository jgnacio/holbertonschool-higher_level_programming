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


if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Make a engine to connect to mysql database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )

    # Create the engine with the given connection
    Base.metadata.create_all(engine)

    # Create new session class and session instance for
    # manage the database.
    Session = sessionmaker(engine)
    session = Session()

    # Print out all the records on state column
    states = session.query(State)
    for state in states:
        print(f"{state.id}: {state.name}")

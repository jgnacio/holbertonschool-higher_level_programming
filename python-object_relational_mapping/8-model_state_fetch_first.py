#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 12:55:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy and lists the
    first State objects from the
    database given.
"""


if __name__ == "__main__":
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

    # Print out only the first row of state table
    state = session.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

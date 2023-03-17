#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 13:16:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy and lists the
    only the states that have an a in
    the name record of State table from
    the given database.
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

    # safe from sql injection
    safe_argument = (sys.argv[4],)

    # Print out only the states that have an a in the name record
    states = session.query(State).filter(State.name.like(safe_argument)).all()

    if states:
        for state in states:
                print(f"{state.id}")
    else:
        print("Not found")

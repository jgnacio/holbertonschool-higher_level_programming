#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 13:30:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy and create a new
    record with in the tables states
    with the name Louisiana.
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

    # Make a new record in the table state
    new_state = State(name="Louisiana")

    # Add to the session
    session.add(new_state)

    # Set all changues
    session.commit()
    print(new_state.id)

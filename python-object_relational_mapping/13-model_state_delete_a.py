#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 13:55:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy to the given
    database and delete all records
    that name contains an "a".
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

    # Get only the row with the id equal to 2
    delete_states = session.query(State).filter(State.name.like("%a%"))

    # Delete all record fetched
    delete_states.delete()
    session.commit()

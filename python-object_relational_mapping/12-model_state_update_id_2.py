#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 13:42:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy to the given
    database and update the row of
    the state table with id equal to 2.
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
    update_state = session.query(State).filter_by(id=2).first()

    # Changue the name record like an argument object
    update_state.name = "Mexico"

    # Set all changues
    session.commit()

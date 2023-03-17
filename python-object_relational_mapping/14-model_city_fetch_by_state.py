#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 14:16:00 2023.

@author: jgnacio
@description:
    This module provide a connection
    with sqlalquemy to the given
    database and join the City.state_id
    to the state.id and print all.
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, join
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    join_id_states = join(City, State, City.state_id == State.id)

    cities = session.query(
        City.name,
        State.name,
        City.state_id
    ).select_from(join_id_states).all()
    for city in cities:
        print(f"{city[1]}: ({city[2]}) {city[0]}")

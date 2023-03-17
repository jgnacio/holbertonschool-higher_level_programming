#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 10:17:00 2023.

@author: jgnacio
@description:
    This module provides a simple connection to
    a Mysql database with MySQLdb module, using
    the comand line arguments.

    That lists all states  that lists all cities
    from the database passed.
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # Trying to connect
    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        # If connection is not successful
    except MySQLdb.OperationalError:
        print("Can't connect to database")

    # Making Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # select all states with the name specified
    query = ("SELECT cities.id, cities.name, states.name " +
             "FROM states INNER JOIN cities " +
             "ON state_id = states.id ORDER BY cities.id")

    # Executing Query
    cursor.execute(query)

    # Above Query Gives Us The Current Date
    # Fetching all Data
    states = cursor.fetchall()

    # Printing Rresult Of Above
    for state in states:
        print(state)

    # Closing Database Connection
    db_connection.close()

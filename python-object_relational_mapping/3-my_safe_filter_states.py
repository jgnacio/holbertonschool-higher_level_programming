#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur March 16 04:32:00 2023.

@author: jgnacio
@description:
    This module provides a simple connection to
    a Mysql database with MySQLdb module, using
    the comand line arguments.

    That lists all states with a name of the 5
    argument passed, and safe from sql injections.
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    # Trying to connect
    try:
        db_connection = MySQLdb.connect(
            "localhost",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
        # If connection is not successful
    except MySQLdb.OperationalError:
        print("Can't connect to database")

    # Making Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # select all states with the name specified
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"

    # make an tuple with only one slot set
    safe_arg = (sys.argv[4],)

    # Executing Query
    cursor.execute(query, safe_arg)

    # Above Query Gives Us The Current Date
    # Fetching all Data
    states = cursor.fetchall()

    # Printing Rresult Of Above
    for state in states:
        print(state)

    # Closing Database Connection
    db_connection.close()

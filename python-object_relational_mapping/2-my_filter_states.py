#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur March 16 04:08:00 2023.

@author: jgnacio
@description:
    This module provides a simple connection to
    a Mysql database with MySQLdb module, using
    the comand line arguments.

    That lists all states with a name of the 5
    argument passed.
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

    # Executing Query
    cursor.execute(
        "SELECT * FROM states where name LIKE BINARY \"{}\" ORDER BY id".format(
            sys.argv[4]
        )
    )

    # Above Query Gives Us The Current Date
    # Fetching all Data
    states = cursor.fetchall()

    # Printing Rresult Of Above
    for state in states:
        print(state)

    # Closing Database Connection
    db_connection.close()
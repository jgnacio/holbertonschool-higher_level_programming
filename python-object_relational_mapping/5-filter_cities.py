#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 17 10:52:00 2023.

@author: jgnacio
@description:
    This module provides a simple connection to
    a Mysql database with MySQLdb module, using
    the comand line arguments.

    Takes in the name of a state as an argument
    and lists all cities of that state, using
    the database given, safe from sql
    injections.
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    except MySQLdb.OperationalError:
        print("Can't connect to database")

    cursor = db_connection.cursor()

    # select all states with the name specified
    query = ("SELECT cities.name " +
             "FROM states INNER JOIN cities " +
             "ON state_id = states.id WHERE states.name = %s")

    # Make safe from sql injections.
    safe_arg = (sys.argv[4],)

    cursor.execute(query, safe_arg)

    states = cursor.fetchall()

    # Printing fetch data with comma separation
    output = ", ".join(state[0] for state in states)
    print(output)

    db_connection.close()

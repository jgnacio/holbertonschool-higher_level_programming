#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur March 16 02:37:00 2023.

@author: jgnacio
@description:

"""

import MySQLdb

def conect_to_db():
    """Function for connecting to MySQL database."""
    # Trying to connect
    try:
        db_connection = MySQLdb.connect("localhost","root","","hbtn_0e_0_usa")
    # If connection is not successful
    except MySQLdb.OperationalError:
        print("Can't connect to database")
        return 0

    # Making Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # Executing Query
    cursor.execute("SELECT * FROM states")

    # Above Query Gives Us The Current Date
    # Fetching all Data
    states = cursor.fetchall()

    # Printing Rresult Of Above
    for state in states:
        print(state)

    # Closing Database Connection
    db_connection.close()


# Function Call For Connecting To Our Database
conect_to_db()

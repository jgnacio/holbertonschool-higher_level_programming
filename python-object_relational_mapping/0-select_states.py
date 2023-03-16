#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import MySQLdb

"""
Created on Thur March 16 02:37:00 2023.

@author: jgnacio
@description:
    This module provides a simple connection to
    a Mysql database with MySQLdb module, using
    the comand line arguments.
"""


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
cursor.execute("SELECT * FROM states")

# Above Query Gives Us The Current Date
# Fetching all Data
states = cursor.fetchall()

# Printing Rresult Of Above
for state in states:
    print(state)

# Closing Database Connection
db_connection.close()

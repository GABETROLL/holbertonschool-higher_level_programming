#!/usr/bin/python3
"""
Logs in database in 'localhost' with
the REQUIRED user, password and database in the
shell arguments provided when starting this script.

Then, it dispays all the rows from the table 'states'
(hopefully) in the supplied database in the last
shell argument, ordered by the 'id' value.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv
    database = MySQLdb.connect("localhost", *argv, 3306)
    cursor = database.cursor()
    cursor.query("SELECT * FROM states ORDER BY id ASC")
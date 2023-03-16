#!/usr/bin/python3
"""
Logs in database in 'localhost' with
the REQUIRED user, password and database in the
shell arguments provided when starting this script.

Lists all states (in the 'states' table')
with a 'name' starting with "N".
from the database with the name provided in the last
shell argument.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv
    database = MySQLdb.connect("localhost", *argv[1:], 3306)
    with database.cursor() as cursor:
        cursor.execute("SELECT * FROM states WHERE id LIKE 'N%' ORDER BY id ASC")
        database.commit()
        result = cursor.fetchall()
        print(result)
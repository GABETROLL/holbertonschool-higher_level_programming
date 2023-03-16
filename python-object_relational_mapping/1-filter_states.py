#!/usr/bin/python3
"""
Usage: ../1-filter_states.py
    <MySQL username>
    <MySQL password>
    <MySQL database>
(all arguments are required, and are
assumed to be there, without any more arguments)

Logs in database in 'localhost' with
the REQUIRED MySQL: 'username', 'password', 'database
name' in the above shell arguments, in port 3306.

Lists all states (in the 'states' table')
with a 'name' (VARCHAR(256)) starting with "N".
The table should also have an id INT column.
from the database with the name provided in the last
shell argument.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv
    database = MySQLdb.connect("localhost", *argv[1:], 3306)
    with database.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )
        # "LIKE BINARY" is case-sensitive.
        database.commit()
        result = cursor.fetchall()
        if result:
            # Empty tuple should make this script
            # print nothing, and
            # also no new line.
            print(*result, sep="\n")

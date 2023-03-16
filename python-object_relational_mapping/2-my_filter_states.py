#!/usr/bin/python3
"""
Usage: ./2-my_filter_states.py <username> <password>
    <database name> <state>
    (all of the arguments are required)

Logs in database in 'localhost' with
the REQUIRED MySQL: 'username', 'password', 'database
name' in the above shell arguments, in port 3306.

Prints all the records in the table named 'states',
in the 'database name' shell argument, that have
their 'name' column value = the 'state' argument.
Prints them ordered by their 'id' value, ascending.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv

    database = MySQLdb.connect("localhost", *argv[1:-1], 3306)
    with database.cursor() as cursor:
        cursor.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY '{}'\
                        ORDER BY id ASC".format(argv[-1]))
        database.commit()
        result = cursor.fetchall()
        if result:
            # Empty tuple should make this script
            # print nothing, and
            # also no new line.
            print(*result, sep="\n")

#!/usr/bin/python3
"""
Usage: ./3-my_filter_states.py
    <MySQL username>
    <MySQL password>
    <MySQL database name>
    <state>
(all arguments are required, and are
assumed to be there, without any more arguments)

Logs in database in 'localhost' with
the REQUIRED MySQL: 'username', 'password', 'database
name' in the above shell arguments, in port 3306.

Prints all the records in the table named 'states',
in the 'database name' shell argument, that have
their 'name' column value = the 'state' argument.
Prints them ordered by their 'id' value, ascending.

BUT the argument 'state' must not contain any symbols,
in order to prevent a MySql injection.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv

    state = argv[-1]
    if any(not c.isalpha() for c in state):
        exit(1)

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

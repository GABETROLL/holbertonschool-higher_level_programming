#!/usr/bin/python3
"""
Usage: ./4-cities_by_state.py
    <MySQL username>
    <MySQL password>
    <MySQL database name>
(all arguments are required, and are
assumed to be there, without any more arguments)

Logs in database in 'localhost' with
the REQUIRED MySQL: 'username', 'password', 'database
name' in the above shell arguments, in port 3306.

'execute' can only be used once in this code.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv
    database = MySQLdb.connect("localhost", *argv[1:], 3306)

    with database.cursor() as cursor:
        cursor.execute("SELECT id,\
                               name,\
                               (SELECT name FROM states\
                                    WHERE states.id=cities.state_id)\
                                    AS state_name\
                        FROM cities ORDER BY id")
        database.commit()
        result = cursor.fetchall()
        if result:
            # Empty tuple should make this script
            # print nothing, and
            # also no new line.
            print(*result, sep="\n")

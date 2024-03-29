#!/usr/bin/python3
"""
Usage: ./0-select_states.py
    <MySQL username>
    <MySQL password>
    <MySQL database>
(all arguments are required, and are
assumed to be there, without any more arguments)

Logs in database in 'localhost' with
the REQUIRED MySQL: 'username', 'password', 'database
name' in the above shell arguments, in port 3306.

Definition:
-----------------------------------
states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
)
-----------------------------------

Then, it dispays all the rows from the table 'states'
(hopefully) in the supplied database in the last
shell argument, ordered by the 'id' value.
"""
import MySQLdb

if __name__ == "__main__":
    from sys import argv
    database = MySQLdb.connect("localhost", *argv[1:], 3306)

    with database.cursor() as cursor:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        database.commit()
        result = cursor.fetchall()
        if result:
            # an empty result shouldn't print anything,
            # not even a new line.
            print(*result, sep="\n")

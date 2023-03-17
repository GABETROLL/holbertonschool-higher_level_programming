#!/usr/bin/python3
"""
Usage: ./7-model_state_fetch_all.py
    <MySQL username>
    <MySQL password>
    <database name>

Selects everything from the table named 'states'
in the database logged in as the user provided
in the arguments. And prints the output.

Definition:
-----------------------------------
states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
)
-----------------------------------
"""
from sqlalchemy import select, create_engine
from model_state import Base, State

if __name__ == "__main__":
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(*argv[1:]))
    connection = engine.connect()

    statement = select(State)
    output = connection.execute(statement)

    print(output)

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
-----------------------d------------
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    from sys import argv

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(*argv[1:])
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(State).order_by(State.id)

    for row in output:
        print(f"{row.id}: {row.name}")

    session.close()

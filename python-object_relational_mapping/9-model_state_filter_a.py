#!/usr/bin/python3
"""
Usage: ./8-model_state_filter_a.py
    <MySQL username>
    <MySQL password>
    <database name>

Prints all the State objects from the table
named 'states', that have their names start with
the letter a, in the database logged in as the
user provided in the arguments. And prints the
output.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import or_, not_
from model_state import Base, State

if __name__ == "__main__":
    from sys import argv

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(*argv[1:])
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(State)\
                    .where(State.name.like("%a%"))

    for row in output:
        print(f"{row.id}: {row.name}")

    session.close()

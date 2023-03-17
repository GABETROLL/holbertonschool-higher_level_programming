#!/usr/bin/python3
"""
Usage: ./8-model_state_filter_a.py
    <MySQL username>
    <MySQL password>
    <database name>
    <state name>

Prints all the State objects from the table
named 'states', that have their names be equal
to the 'state name' shell argument.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import or_, not_
from model_state import Base, State

if __name__ == "__main__":
    from sys import argv

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(*argv[1:-1])
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    name_to_find = argv[-1]
    output = session.query(State).filter_by(name=name_to_find)

    if output:
        for row in output:
            print(f"{row.id}: {row.name}")
    else:
        print("Not found")

#!/usr/bin/python3
"""
Usage: ./8-model_state_fetch_first.py
    <MySQL username>
    <MySQL password>
    <database name>

Prints the first State object from the table
named 'states' in the database logged in as the
user provided in the arguments. And prints the
output.

Fecthing all the states before printing the first
one is not allowed.

If the 'states' table is empty, the output printed
by this script is "Nothing", followed by a new line.
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

    output = session.query(State).filter(id=1)

    for row in output:
        print(f"{row.id}: {row.name}")
        break
    else:
        print("Nothing")

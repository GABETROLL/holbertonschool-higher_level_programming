#!/usr/bin/python3
"""
Exercise 6: Make a class called 'State' that
links to a MySQL table 'states'.

Definition:
states (id INT PRIMARY KEY, name )
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, create_engine
Base = declarative_base()


class State(Base):
    __table_name__ = "states"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", VARCHAR(128), not_null=True)

#!/usr/bin/python3
"""
Exercise 6: Make a class called 'State' that
links to a MySQL table 'states'.

Definition:
states (id INT PRIMARY KEY, name )
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
Base = declarative_base()


class State(Base):
    """
    States table with name and id
    """
    __table_name__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), not_null=True)

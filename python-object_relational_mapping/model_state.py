#!/usr/bin/python3
"""
Exercise 6: Make a class called 'State' that
links to a MySQL table 'states'.

Definition:
states (id INT PRIMARY KEY, name )
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """
    States table with name and id
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)

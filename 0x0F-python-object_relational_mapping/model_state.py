#!/usr/bin/python3
""" This script shall contain def of state and base instance """
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """THis class shall represent state class
    Attributes:
    __tablename__: the tablename of cls
    id: this hsall represent state id
    name: this shall represent state name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""This script shall print all city objects from db"""
import sys
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_u = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])
    eng = create_engine(db_u, pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

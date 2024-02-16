#!/usr/bin/python3
""" This code shall list all states with letter a from database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    db_u = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                       sys.argv[2],
                                                       sys.argv[3])
    eng = create_engine(db_u, pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()
    for state in session.query(State).filter(State.name.like(
            '%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

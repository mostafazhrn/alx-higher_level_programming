#!/usr/bin/python3
""" This code shall list all states from database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

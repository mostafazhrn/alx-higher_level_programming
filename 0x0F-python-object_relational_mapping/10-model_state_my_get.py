#!/usr/bin/python3
"""this script shall print state with name passed as arg in db"""
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
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if state is None else "{}".format(state.id))

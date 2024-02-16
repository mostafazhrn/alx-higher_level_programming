#!/usr/bin/python3
"""This script shall change the name of state object in db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    db_u = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])
    eng = create_engine(db_u, pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()
    stt = session.query(State).filter(State.id == 2).first()
    stt.name = 'New Mexico'
    session.commit()
    session.close()

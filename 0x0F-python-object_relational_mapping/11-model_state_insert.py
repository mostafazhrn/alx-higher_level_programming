#!/usr/bin/python3
"""This code shall add state obj Louisiana to db"""
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
    new_stt = State(name='Louisiana')
    session.add(new_stt)
    session.commit()
    print(new_stt.id)
    session.close()

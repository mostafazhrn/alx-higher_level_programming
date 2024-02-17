#!/usr/bin/python3
""" This code shall list all cities from the database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City, Base

if __name__ == "__main__":
    db_u = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])
    eng = create_engine(db_u, pool_pre_ping=True)
    Sesh = sessionmaker(bind=eng)
    session = Sesh()
    new_stt = State(name='California')
    new_ct = City(name='San Francisco')
    new_stt.cities.append(new_ct)
    session.add(new_stt)
    session.commit()
    session.close()

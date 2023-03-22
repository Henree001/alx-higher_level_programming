#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""


import sys
from sqlalchemy import create_engine, select
from model_state import Base, State
from sqlalchemy.orm import Session
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    with Session(engine) as session:
        txt = select(City, State).join(State)
        rows = session.execute(txt)
        for city, state in rows:
            print("{}: ({:d}) {}".format(state.name, city.id, city.name))

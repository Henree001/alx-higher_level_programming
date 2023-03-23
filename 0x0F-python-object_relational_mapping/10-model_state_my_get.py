#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as argument
from the database `hbtn_0e_6_usa`.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))
    with Session(engine) as session:
        txt = select(State).filter(State.name == '{}'.format(sys.argv[4]))
        row = session.execute(txt).first()
        if row is None:
            print('Not found')
        else:
            for i in row:
                print(i.id)

#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))
    with Session(engine) as session:
        new_object = State(name='Louisiana')
        session.add(new_object)
        session.commit()

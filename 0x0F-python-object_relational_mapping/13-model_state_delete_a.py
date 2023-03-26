#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))
    with Session(engine) as session:
        txt = select(State).filter(State.name.contains('a'))
        rows = session.execute(txt).all()
        for row in rows:
            session.delete(row)

        session.commit()

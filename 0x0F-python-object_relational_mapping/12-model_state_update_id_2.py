#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    with Session() as session:
        txt = select(State).where(State.id == '2')
        row = session.execute(txt).first()
        for item in row:
            item.name = "New Mexica"
        session.commit()

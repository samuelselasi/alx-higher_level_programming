#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """Function that connects to MySQL server on localhost at port 3306"""

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2],
                                                          argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    update_id = 2
    new_name = "New Mexico"
    result = session.query(State).filter(State.id == update_id)
    for row in result:
        row.name = new_name
    session.commit()
    session.close()

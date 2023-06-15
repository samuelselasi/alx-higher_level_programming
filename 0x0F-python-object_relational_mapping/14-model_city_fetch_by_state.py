#!/usr/bin/python3
"""A script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    """Function that connects to MySQL server on localhost at port 3306"""

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2],
                                                          argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).order_by(City.id)
    result = query.all()
    for row in result:
        print("{:s}: ({:d}) {:s}".format(*row))
    session.commit()
    session.close()

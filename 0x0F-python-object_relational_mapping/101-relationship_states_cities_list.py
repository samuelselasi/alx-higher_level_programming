#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    """Function that connects to MySQL server on localhost at port 3306"""

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2],
                                                          argv[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    result = query.all()
    for state in result:
        print("{:d}: {:s}".format(state.id, state.name))
        for cities in state.cities:
            print("\t{:d}: {:s}".format(cities.id, cities.name))
    session.commit()
    session.close()

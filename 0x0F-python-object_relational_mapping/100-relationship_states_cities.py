#!/usr/bin/python3
"""
A script that creates the State California with the City San Francisco
from the database hbtn_0e_100_usa
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
    new_sname = "California"
    new_cname = "San Francisco"
    new_state = State(name=new_sname)
    new_city = City(name=new_cname)
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()

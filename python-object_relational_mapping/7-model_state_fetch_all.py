#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri March 19 12:50:00 2023.

@author: Agustin3100
@description:
Lists all state objects on hbtn database.
"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Connect to mysql database throguh engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))

    # Create engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print records
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

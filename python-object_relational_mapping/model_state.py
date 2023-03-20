#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri March 17 11:29:00 2023.

@author: Agustin
@description:
    This module if for declaration of
    State class that have this columns:
        (id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(128) NOT NULL)
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.create_all(engine)


class State(Base):
    """State class with name and id."""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)


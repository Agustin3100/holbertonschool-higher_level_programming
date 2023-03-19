#!/usr/bin/python3
"""First state model."""


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

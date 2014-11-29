from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_jobs_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Jobs(DeclarativeBase):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title    = Column('title', String)
    link     = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    company  = Column('company', String, nullable=True)
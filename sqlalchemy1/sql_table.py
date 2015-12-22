#
# Title:sql_table.py
# Description: SQLAlchemy adapter
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime

from sqlalchemy import Column
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)
    name_fk = Column(Integer)
    street1 = Column(String)
    street2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

    def __init__(self, name_fk, street1, street2, city, state, zip):
        self.name_fk = name_fk
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip = zip

    def __repr__(self):
        return "<address(%d, %d)>" % (self.id, self.name_fk)

class Name(Base):
    __tablename__ = 'name'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<name(%d, %s)>" % (self.id, self.name)
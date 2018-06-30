#! /usr/bin/python3
#
# Title:test1.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, String

Base = declarative_base()

class Table1(Base):
    __tablename__ = 'table1'

    id = Column(BigInteger, primary_key=True)
    time_stamp = Column(DateTime, default=datetime.datetime.utcnow)
    column1 = Column(String(32))

#    def __init__(self, task_id, table_name, population):
#        self.task_id = task_id
#        self.table_name = table_name
#        self.population = population

    def __repr__(self):
        return "<Table1(%s)>" % (self.column1)

class SqlAlchemyTest1:

    def __init__(self):
        mysql_username = 'gsc'
        mysql_password = 'bogus'
        mysql_hostname = 'localhost'
        mysql_database = 'playpen'

        self.mysql_url = "mysql://%s:%s@%s:3306/%s" % (mysql_username, mysql_password, mysql_hostname, mysql_database)

    def execute(self):
        print('execute')

        engine = create_engine(self.mysql_url, echo=False)
        Base.metadata.create_all(engine)

        session = sessionmaker()
        session.configure(bind=engine)
        ss = session()

#        Session = sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)

        t1 = Table1(column1='test1')
        print(t1)

        result = ss.add(t1);
        print(result)

        result = ss.commit()
        print(result)

        print(t1.id)
        print(t1.time_stamp)


print('start sa3test1');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print(sqlalchemy.__version__);

    driver = SqlAlchemyTest1()
    driver.execute()

print('stop sa3test1');

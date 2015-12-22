#! /usr/bin/python
#
# Title:sa_reader.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import random
import sys
import time
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_table import Address
from sql_table import Name

class Reader:

    def execute1(self, population, session):
        for ndx in range(population):
            if (ndx > 0) and (ndx % 1000) == 0:
                print ndx

            selected_set = session.query(Name).filter_by(id = ndx).all()
            for selected in selected_set:
                if selected.id != ndx:
                    print "select failure:%d" % (ndx)

    def execute2(self, population, session):
        for ndx in range(population):
            if (ndx > 0) and (ndx % 1000) == 0:
                print ndx

            selected_set = session.query(Name).filter_by(id = ndx).all()
            for selected in selected_set:
                if selected.id != ndx:
                    print "select failure:%d" % (ndx)

            selected_set = session.query(Address).filter_by(name_fk = ndx).all()
            for selected in selected_set:
                if selected.name_fk != ndx:
                    print "select failure:%d" % (ndx)

    def execute3(self, population, session):
        for ndx in range(population):
            if (ndx > 0) and (ndx % 1000) == 0:
                print ndx

            target = random.randint(0, population)

            selected_set = session.query(Name).filter_by(id = target).all()
            for selected in selected_set:
                if selected.id != target:
                    print "select failure:%d" % (target)

print 'start SQL Alchemy Reader'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        yaml_filename = sys.argv[1]
    else:
        yaml_filename = 'config.yaml'

    configuration = yaml.load(file(yaml_filename))

    mysql_username = configuration['mySqlUserName']
    mysql_password = configuration['mySqlPassWord']
    mysql_hostname = configuration['mySqlHostName']
    mysql_database = configuration['mySqlDataBase']

    mysql_url = "mysql://%s:%s@%s:3306/%s" % (mysql_username, mysql_password, mysql_hostname, mysql_database)

    engine = create_engine(mysql_url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    start_time = time.time()

    population = 1000000
    population = 10000

    driver = Reader()
    driver.execute2(population, session)

    stop_time = time.time()
    duration = stop_time - start_time
    log_message = "loader stop w/population %d and duration %d" % (population, duration)
    print(log_message)

print 'stop SQL Alchemy Reader'

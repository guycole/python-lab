#! /usr/bin/python
#
# Title:session_sql_dump.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os

print 'start'

for ndx in range(1, 4991462):
    command = "echo \"select * from price_session where name_id = %d order by date;\" | mysql -u root -pbogus mythic_recorder_v1 > /mnt/raid0/gsc/archiver/session%d.txt" % (ndx, ndx)
    print command
    os.system(command)

print 'stop'
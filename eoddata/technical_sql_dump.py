#! /usr/bin/python
#
# Title:technical_sql_dump.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import os

print 'start'

for ndx in range(1, 4991462):
    command = "echo \"select * from technical where name_id = %d order by tar_file_name;\" | mysql -u root -pbogus mythic_recorder_v1 > /mnt/raid0/gsc/tech/techie%d.txt" % (ndx, ndx)
    print command
    os.system(command)

print 'stop'

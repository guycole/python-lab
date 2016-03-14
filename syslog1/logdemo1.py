#! /usr/bin/python
#
# Title:logger1.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import random
import syslog

class LogDemo:

    def random_string(self):
        return "%x" % (random.randint(0, 1e15))

    def execute(self):
        syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL3)
        syslog.syslog(self.random_string())
        syslog.syslog(syslog.LOG_DEBUG, 'debug')
        syslog.syslog(syslog.LOG_INFO, 'info')
        syslog.syslog(syslog.LOG_NOTICE, 'notice')
        syslog.syslog(syslog.LOG_WARNING, 'warning')
        syslog.syslog(syslog.LOG_ERR, 'err')
        syslog.syslog(syslog.LOG_CRIT, 'crit')
        syslog.syslog(syslog.LOG_ALERT, 'alert')
        syslog.syslog(syslog.LOG_EMERG, 'emerg')

        syslog.closelog()

print 'start logdemo1'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    driver = LogDemo()
    driver.execute()

print 'stop logdemo1'

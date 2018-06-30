#! /usr/bin/python3
#
# Title:mindlance2.py
# Description: hash demo
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import operator

class MindLance:

    def execute(self):
        print("execute")

        last_name = {}
        last_name['Mary'] = 'Li'
        last_name['James'] = 'O\'Day'
        last_name['Thomas'] = 'Miller'
        last_name['William'] = 'Garcia'
        last_name['Elizabeth'] = 'Davis'

        name_length = {}
        for key in last_name:
            name_length[key] = len(last_name[key])

        name_length_list = sorted(name_length.items(), key=lambda x:x[1])

        print("sorted by length of last name")
        for temp in name_length_list:
            key = temp[0]
            print("%s %s" % (key, last_name[key]))

        print("sorted by first name")
        for key in sorted(last_name.keys()):
            print("%s %s" % (key, last_name[key]))


print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    driver = MindLance()
    driver.execute()

print('stop')

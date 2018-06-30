#! /usr/bin/python3
#
# Title:mindlance1.py
# Description: character frequency counter
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
class MindLance:

    def execute(self, candidate):
        print("execute")

        results = {}

        candidates = list(candidate)
        for ndx in candidates:
            if ndx in results:
                results[ndx] = 1 + results[ndx]
            else:
                results[ndx] = 1

        for ndx in results:
            population = results[ndx]
            buffer = '#'*population
            print("%s %d %s" % (ndx, population, buffer))

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    driver = MindLance()
    driver.execute("Mississippi borders Tennessee.")

print('stop')

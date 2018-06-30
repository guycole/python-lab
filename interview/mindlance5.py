#! /usr/bin/python3
#
# Title:mindlance5.py
# Description: json comment stripper
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#


class MindLance:

    def execute(self, arg):
        results = []
        for row in arg:
            flag = True
            temp = list(row)
            for ndx1 in range(len(temp)):
                if temp[ndx1] == '/' and temp[ndx1+1] == '/':
                    if temp[ndx1-1] != ':':
                        flag = False
                        buffer = row[:ndx1]
                        if (len(buffer) > 0):
                            results.append(buffer)

            if flag is True:
                results.append(row)

        return results

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    buffer = [
        "// this is a comment",
        "{ // another comment",
        "true, \"foo\", //3rd comment",
        "\"http://www.ariba.com\" //comment after URL",
        "}"
    ]

    driver = MindLance()
    print(driver.execute(buffer))

print('stop')

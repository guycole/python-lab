#! /usr/bin/python3
#
# Title:rangoli1.py
# Description: generate a rangoli pattern
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#

def print_rangoli(size):
    alphabet = []
    for ndx in range(26):
        alphabet.append(chr(97 + ndx))

    output1 = []
    for row in range(1, size+1):
        buffer = ''
        for ndx in range(size-row, size):
            buffer = buffer + alphabet[ndx]

        output1.append(buffer)

    #
    # pass1 complete w/partial strings created
    # pass2 will create full string
    #
    output2 = []
    for row in range(len(output1)):
        buffer1 = list(output1[row])
        buffer1.sort()

        buffer2 = list(output1[row])
        buffer2.reverse()

        if len(buffer1) == 1:
            output2.append(buffer1)
        else:
            output2.append(buffer2 + buffer1[1:])

    #
    # pass3 adds dashes
    #
    output3 = []
    max_length = -1
    for row in range(len(output2)-1, -1, -1):
        buffer = ''
        for column in range(len(output2[row])):
            buffer = buffer + (output2[row][column]) + '-'

        temp = buffer[:len(buffer)-1]
        if len(output3) < 1:
            max_length = len(temp)
        else:
            while len(temp) < max_length:
                temp = '-' + temp + '-'

        output3.append(temp)

    #
    # display
    #
    output3.reverse()
    for row in range(len(output3)):
        print(output3[row])

    for row in range(len(output3)-2, -1, -1):
        print(output3[row])

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    print_rangoli(5)

print('stop')

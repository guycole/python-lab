#! /usr/bin/python3
#
# Title:mindlance3.py
# Description: paren balance
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

class MindLance:

    def execute(self, arg):
        stack = Stack()

        candidates = list(arg)

        for ndx in candidates:
            if ndx == '(':
                stack.push(ndx)
            elif ndx == ')':
                if stack.is_empty():
                    return 'unbalanced'
                if stack.peek() == '(':
                    stack.pop()
                else:
                    return 'unbalanced'
            elif ndx == '[':
                stack.push(ndx)
            elif ndx == ']':
                if stack.is_empty():
                    return 'unbalanced'
                if stack.peek() == '[':
                    stack.pop()
                else:
                    return 'unbalanced'
            elif ndx == '{':
                stack.push(ndx)
            elif ndx == '}':
                if stack.is_empty():
                    return 'unbalanced'
                if stack.peek() == '{':
                    stack.pop()
                else:
                    return 'unbalanced'

        if stack.is_empty():
            return 'balanced'
        else:
            return 'unbalanced'

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    driver = MindLance()
    print(driver.execute('()[]{}'))
    print(driver.execute('[]{}'))
    print(driver.execute('([])'))
    print(driver.execute('([)]'))
    print(driver.execute('](){'))

print('stop')

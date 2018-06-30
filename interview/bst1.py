#! /usr/bin/python3
#
# Title:rotate_right1.py
# Description: circular rotate right of array
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.value < node.value:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)

    def dumper(self, root):
        if root is not None:
            self.dumper(root.left)
            print(root.value)
            self.dumper(root.right)

print('start');

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    print('main')

    root = Node(50)
    bst = BinarySearchTree()
    bst.insert(root, Node(30))
    bst.insert(root, Node(20))
    bst.insert(root, Node(40))
    bst.insert(root, Node(70))
    bst.insert(root, Node(60))
    bst.insert(root, Node(80))
    bst.dumper(root)

print('stop')

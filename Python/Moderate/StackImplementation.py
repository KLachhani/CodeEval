__author__ = 'Kishan'

import sys

class integerstack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self, i):
        return self.items.pop(i)

    def size(self):
        return len(self.items)


stacks = open('StackImplementation')

for line in stacks:
    stack = integerstack()
    elem = line.split(' ')
    for x in elem:
        stack.push(int(x.rstrip()))

    i = stack.size()-1
    while i >= 0:
        sys.stdout.write(str(stack.pop(i)) + ' ')
        i -= 2
    sys.stdout.write('\n')






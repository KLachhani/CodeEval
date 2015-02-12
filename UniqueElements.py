__author__ = 'Kishan'

import sys

def contains(list, x):
    for i in list:
        if i == x:
            return True
    return False

lists = open(sys.argv[1])

for line in lists:
    l = line.split(',')
    uniq = []
    for i in l:
        if not contains(uniq, i.rstrip()):
            uniq.append(str(i.rstrip()))


    sys.stdout.write(','.join(uniq) + '\n')

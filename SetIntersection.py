__author__ = 'Kishan'

import sys

def contains(list, x):
    for i in list:
        if i == x:
            return True
    return False

f = open(sys.argv[1])

for line in f:
    twolists = line.split(';')
    list1 = twolists[0].split(',')
    list2 = twolists[1].split(',')

    intersections = []
    for i in list2:
        if contains(list1, i.rstrip()):
            intersections += [i.rstrip()]

    if len(intersections) == 0:
        sys.stdout.write('\n')
    else:
        sys.stdout.write(','.join(intersections) + '\n')
__author__ = 'Kishan'

import sys
lines = open('MthToLastElement')

for line in lines:
    l = line.split(' ').reverse()
    print l[0]

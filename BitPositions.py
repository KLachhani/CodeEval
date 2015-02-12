__author__ = 'Kishan'

import sys
file = open(sys.argv[1])
for line in file:
    n = int(line.split(',')[0])
    p1 = int(line.split(',')[1])
    p2 = int(line.split(',')[2])
    n = str(bin(n))[::-1]
    if n[p1-1] == n[p2-1]:
        sys.stdout.write('true\n')
    else:
        sys.stdout.write('false\n')


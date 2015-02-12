__author__ = 'Kishan'

import sys
file = open(sys.argv[1])
for line in file:
    line = line.rstrip()
    sum = 0
    for i in line:
        sum += int(i)
    sys.stdout.write(str(sum) + '\n')


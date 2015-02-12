__author__ = 'Kishan'

import sys
file = open(sys.argv[1])
for line in file:
    sys.stdout.write(line.lower() + '\n')
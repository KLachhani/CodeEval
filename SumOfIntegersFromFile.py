__author__ = 'Kishan'

import sys
integers = open(sys.argv[1])

sum = 0
for i in integers:
    sum += int(i.rstrip())

sys.stdout.write(str(sum))
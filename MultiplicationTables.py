__author__ = 'Kishan'

import sys
for x in range(1, 13):
    for y in range(1, 13):
        sys.stdout.write(str(x*y).rjust(4))
    sys.stdout.write('\n')
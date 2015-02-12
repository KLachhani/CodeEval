__author__ = 'Kishan'

import sys
file = open(sys.argv[1])
for line in file:
    x = int(line.split(',')[0])
    n = int(line.split(',')[1])

    i = 1
    ans = 0
    while ans < x:
        ans += n
        i += 1
    sys.stdout.write(str(ans) + '\n')
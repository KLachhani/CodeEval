__author__ = 'Kishan'

import sys
test_cases = open('FizzBuzz.txt', 'r')
for test in test_cases:
    x = int(test.split(' ')[0])
    y = int(test.split(' ')[1])
    n = int(test.split(' ')[2])
    for i in range(1, n+1):
        if i % x == 0:
            sys.stdout.write('F')
        if i % y == 0:
            sys.stdout.write('B')
        if (i % x != 0) & (i % y != 0):
            sys.stdout.write(str(i))
        sys.stdout.write(' ')
    print

test_cases.close()
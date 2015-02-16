__author__ = 'Kishan'

import sys
test_case = open(sys.argv[1])
lines = []

for test in test_case:
    lines += [test.rstrip()]

n = int(lines[0])
lines.sort(key=lambda line: len(line), reverse=True)

for i in range(0,n):
    sys.stdout.write(lines[i] + '\n')
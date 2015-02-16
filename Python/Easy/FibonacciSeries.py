__author__ = 'Kishan'

import sys

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


lines = open(sys.argv[1])
for line in lines:
    n = int(line.rstrip())
    sys.stdout.write(str(Fibonacci(n)) + '\n')
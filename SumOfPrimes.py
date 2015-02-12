__author__ = 'Kishan'

import sys
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
n = 0
i = 2
while n < 1000:
    if isPrime(i):
        sum += i
        n += 1
    i += 1

sys.stdout.write(str(sum))
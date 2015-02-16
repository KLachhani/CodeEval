__author__ = 'Kishan Lachhani'

import sys
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

for i in range(1000, 0, -1):
    if isPalindrome(i) & isPrime(i):
        sys.stdout.write(str(i))
        break
__author__ = 'Kishan'

import sys
def contains(list, n):
    for i in list:
        if i == n:
            return True
    return False

def add(n, list):
    if contains(list, n) == False:
        list += [n]

sequences = open(sys.argv[1])
for s in sequences:
    seq = s.rstrip('\n').split(' ')
    seq_int = []
    for i in range(0, len(seq)):
        seq_int += [int(seq[i])]

    cycle = []
    set = []
    for i in seq_int:
        l = len(set)
        add(i, set)
        if l == len(set):
            add(i, cycle)

    c = ' '.join(str(x) for x in cycle)
    sys.stdout.write(c + '\n')
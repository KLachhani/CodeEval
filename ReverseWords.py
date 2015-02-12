__author__ = 'Kishan'

import sys

sentences = open('ReverseWords.txt')
for s in sentences:
    words = s.split(' ')[::-1]
    for i in range(0, len(words)):
        sys.stdout.write(words[i].rstrip('\n') + ' ')
    sys.stdout.write('\n')

sentences.close()
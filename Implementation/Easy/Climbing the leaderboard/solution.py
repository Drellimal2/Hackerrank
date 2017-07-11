#!/bin/python3

import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
scores_set = []
prev = -1
for score in scores:
    if score == prev:
        continue
    scores_set.append(score)
    prev = score
del prev
# scores_set = list(set(scores)).sort(reverse=True)
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
pos = len(scores_set)
for ali in alice:
    if pos == 0:
        print(1)
        continue
    while ali >= scores_set[pos-1] and pos != 0:
        
        pos -= 1
    print(pos+1)
# your code goes here
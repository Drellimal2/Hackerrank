#!/bin/python3

import sys

def solve(a, b):
    aw = 0 #Alice's wins
    bw = 0 #Bob's wins
    # Complete this function
    for i in range(3):
        if a[i] > b[i]:
            aw += 1
        elif b[i] > a[i]:
            bw += 1
    return aw, bw
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
result = solve(a, b)
print (" ".join(map(str, result)))
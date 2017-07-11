#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 1
    for i in range(n):
        if i % 2 == 0:
            res *= 2
        else:
            res += 1
    print(res)
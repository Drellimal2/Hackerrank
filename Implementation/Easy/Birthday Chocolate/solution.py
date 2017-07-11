#!/bin/python3

import sys

def solve(n, s, d, m):
    if n < m:
        return 0
    res = 0
    strt = 0
    sm = sum(s[:m-1])
    for i in range(m-1, n):
        sm += s[i]
        sm -= strt
        strt = s[i+1 - m]
        if sm == d:
            res += 1
    return res
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
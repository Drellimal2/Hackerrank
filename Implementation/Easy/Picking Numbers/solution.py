#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
d = dict()
for x in a:
    d[x] = d.get(x, 0) + 1
mx = 0
for k in d:
    mx = max(d[k] + d.get(k+1, 0), mx)
print(mx)
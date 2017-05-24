#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d = set(c)
res = 0
for x in d:
    res += c.count(x)//2
print(res)
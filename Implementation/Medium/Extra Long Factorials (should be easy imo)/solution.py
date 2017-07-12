#!/bin/python3

import sys


n = int(input().strip())
res = 1
for i in range(1, n+1):
    res *= i
print(res)
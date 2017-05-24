#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
vals = sorted([(0 - x, types.count(x)) for x in range(1,6)], key= lambda x: (x[1], x[0]), reverse=True)
print(0 -vals[0][0])
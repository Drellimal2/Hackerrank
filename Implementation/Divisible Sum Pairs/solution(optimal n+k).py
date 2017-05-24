#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
mods = {i : 0 for i in range(k)}
for x in a:
    mods[x%k] += 1
res = (mods[0] * (mods[0] - 1))//2
hlf = (k-1)//2

for i in range(1, hlf+ 1):
    res += mods[i] * mods[k-i]
if k %2 == 0:
    res += (mods[k//2] * (mods[k//2] -1))//2
print(res)
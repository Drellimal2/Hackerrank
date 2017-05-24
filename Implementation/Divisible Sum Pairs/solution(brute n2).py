#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (a[i] + a[j]) % k == 0:
            res += 1
print(res)
#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
k = k % n
b = a[n-k:] + a[:n-k]
for a0 in range(q):
    m = int(input().strip())
    print(b[m])
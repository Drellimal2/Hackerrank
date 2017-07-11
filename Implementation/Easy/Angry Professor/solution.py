#!/bin/python3

import sys

RESULT_YES = "YES"
RESULT_NO = "NO"

def cond(x):
    if x <= 0:
        return 1
    else:
        return 0

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [cond(int(a_temp)) for a_temp in input().strip().split(' ')]
    if sum(a) >= k:
        print(RESULT_NO)
    else:
        print(RESULT_YES)
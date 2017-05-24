#!/bin/python3

import sys

def getRecord(s):
    mn = s[0]
    mx = s[0]
    mx_c = 0
    mn_c = 0
    for i in range(1, len(s)):
        if s[i] > mx:
            mx = s[i]
            mx_c += 1
        elif s[i] < mn:
            mn = s[i]
            mn_c += 1
    return mx_c, mn_c
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
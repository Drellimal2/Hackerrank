#!/bin/python3

import sys


n = int(input().strip())
pos = 0
neg = 0
zer = 0
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for element in arr:
    if element == 0:
        zer += 1
    elif element > 0:
        pos += 1
    else:
        neg += 1
print(pos/n)
print(neg/n)
print(zer/n)
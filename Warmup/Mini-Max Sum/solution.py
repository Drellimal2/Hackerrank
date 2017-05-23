#!/bin/python3

import sys

arr = sorted(list(map(int, input().strip().split(' '))))
print( sum(arr[:4]), sum(arr[-4:]))
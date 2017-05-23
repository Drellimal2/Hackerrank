#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
mx = max(height)
print(height.count(mx))
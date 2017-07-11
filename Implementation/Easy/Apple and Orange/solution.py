#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
apples = 0
oranges = 0
for app in apple:
    if s <= app + a <= t:
        apples += 1
print(apples)

for ora in orange:
    if s <= ora + b <= t:
        oranges += 1
print(oranges)
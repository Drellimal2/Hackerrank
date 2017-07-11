#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    mx = -1
    for keyboard in keyboards:
        if keyboard >= s:
            continue
        for drive in drives:
            if drive + keyboard > s:
                continue
            mx = max(mx, drive + keyboard)
    return mx
                
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
#!/bin/python3

import sys


time_str = input().strip()
time, am_pm = time_str[:-2], time_str[-2:]
hr, mn, sc = time.split(":")
if hr == '12':
    hr = '00'
if am_pm == "PM":
    
    hr = str(int(hr) + 12)

time = ":".join([hr, mn, sc])

        
print(time)
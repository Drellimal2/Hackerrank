#!/bin/python3

import sys

day1918 = "26.09.1918"
dayleap = "12.09."
daynonleap = "13.09."

def is_leap(year):
    if year % 4 == 0:
        if year < 1918:
            return True
        if year % 400 == 0 or year % 100 != 0:
            return True
        return False
    else:
        return False

def solve(year):
    # Complete this function
    if year == 1918:
        return day1918
    if is_leap(year):
        return dayleap + str(year)
    return daynonleap + str(year)

year = int(input().strip())
result = solve(year)
print(result)
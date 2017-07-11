#!/bin/python3

import sys

def solve(grades,n):
    # Complete this function
    for i in range(n):
        if grades[i] < 38:
            continue
        if grades[i] % 5 == 0:
            continue
        mul = grades[i] // 5 + 1
        if mul * 5 - grades[i] < 3:
            grades[i] = mul * 5
    return grades
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades,n)
print ("\n".join(map(str, result)))

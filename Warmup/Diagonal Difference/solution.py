#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
diag_sum_1 = 0
diag_sum_2 = 0
for i in range(n):
    diag_sum_1 += a[i][i]
    diag_sum_2 += a[i][n-i-1]
print( abs(diag_sum_1 - diag_sum_2))
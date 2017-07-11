#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function

    s2 = s - 2  # Minus 2 because: 1 is due to index starting from 1 and not 0 
                #and the other one because the starting index is inclusive.
    end = (s2 + m)%n
    end += 1
    return end

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
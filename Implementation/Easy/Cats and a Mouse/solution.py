#!/bin/python3

import sys

CAT_A = "Cat A"
CAT_B = "Cat B"
MOUSE_C = "Mouse C"

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    dx = abs(x - z)
    dy = abs(y - z)
    if dx < dy:
        print(CAT_A)
    elif dx > dy:
        print(CAT_B)
    else:
        print(MOUSE_C)
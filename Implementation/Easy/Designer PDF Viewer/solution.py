#!/bin/python3

import sys
import string

h = list(map(int, input().strip().split(' ')))
letter_dict = dict(zip(string.ascii_lowercase,h))

word = input().strip()

mx_h = letter_dict[max(word, key=lambda x: letter_dict[x])]
print(len(word) * mx_h)
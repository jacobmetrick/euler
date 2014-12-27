#!/usr/bin/python
import math

def isNatural(x):
    return x - math.floor(x) == 0 

for a in range(1, 500):
    for b in range(1, a):
        c = math.sqrt(a * a + b * b)
        if not isNatural(c):
            continue
        if (a + b + c == 1000):
            print(a * b * c)
            exit(0) 

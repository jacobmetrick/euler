#!/usr/bin/python
import math

limit = 20
factors = list(range(limit, 1, -1)) 

for i in factors: 
    for j in factors:
        if j >= i:
            continue
        if (i % j == 0):
            print("i is " + str(i))
            print("j is " + str(j))
            if j in factors:
                factors.remove(j)
            if math.floor(i / j) in factors:
                factors.remove(math.floor(i / j)) 

answer = 1
for i in factors:
    answer *= i

print(answer)

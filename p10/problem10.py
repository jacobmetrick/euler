#!/usr/bin/python
import math

limit = 2000000
primes = [2]
result = 2

for candidate in range(3, limit):
    naturallyTerminated = True
    #testNumber = math.floor(math.sqrt(candidate))
    for i in primes:
        if i > math.floor(math.sqrt(candidate)):
            break
        if candidate % i == 0:
            naturallyTerminated = False
            break
    if naturallyTerminated:
        print(candidate)
        primes.append(candidate) 
        result += candidate

print(result)

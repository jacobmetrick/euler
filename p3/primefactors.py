#!/usr/bin/python
import math

number = 600851475143
primefactors = set()


for possiblefactor in range(2, math.floor(math.sqrt(number))):
    if (number % possiblefactor == 0):
        primefactors.add(possiblefactor)
        number /= possiblefactor
        possiblefactor = 2
    if possiblefactor == math.floor(math.sqrt(number)):
        primefactors.add(possiblefactor) 

output = 0
for i in primefactors:
    if i > output:
        output = i

print(output)


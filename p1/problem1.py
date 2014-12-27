#!/usr/bin/python

addables = []
for i in range(1000): 
    if (i % 3 == 0) or (i % 5 == 0):
        addables.append(i)

value = 0
for i in addables:
    value += i

print(value)

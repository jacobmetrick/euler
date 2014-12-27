#!/usr/bin/python

i1 = 1
i2 = 1
addable = []
while i2 < 4000000:
    tmp = i1 + i2
    i1 = i2
    i2 = tmp 
    if (i2 % 2 == 0):
        addable.append(i2)

value = 0
for i in addable: 
    value += i

print(value)

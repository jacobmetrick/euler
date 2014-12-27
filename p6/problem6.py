#!/usr/bin/python

upto = 100
a = 0
for i in range(1, upto + 1):
    a += (i * i)

b = 0
for i in range(1, upto + 1):
    b += i

b *= b

print(str(b - a))

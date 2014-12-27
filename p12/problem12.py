#!/usr/bin/python
import math

number = nth = 1
while True: 
    divisors = 0 
    root = math.floor(math.sqrt(number))
    for i in range(1, root + 1):
        if number % i == 0:
            if i == root:
                divisors += 1
            else:
                divisors += 2
    if divisors >= 500:
        print(number)
        break
    nth += 1
    number += nth 

#!/usr/bin/python

candidate = 20
while True: 
    for i in range(20, 0, -1):
        if (candidate % i != 0):
            candidate += 20
            break
        if i == 1:
            print(candidate)
            exit(0)

#!/usr/bin/python

answer = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        candidate = i * j
        if candidate < answer:
            break
        if str(candidate) == str(candidate)[::-1]: 
            answer = candidate 

print(answer)

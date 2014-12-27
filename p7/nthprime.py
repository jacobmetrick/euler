#!/usr/bin/python

n = 10001
primes = [2] 

candidate = 3
while len(primes) < n: 
    endedNaturally = True
    for i in primes:
        if (candidate % i == 0):
            endedNaturally = False
            break
    if endedNaturally:
        primes.append(candidate)
        print(candidate)
    candidate += 1

print(primes[-1])

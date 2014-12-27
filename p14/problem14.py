#!/usr/bin/python

chains = {1 : 1}

bestVal = 1
bestNum = 1
for i in range(2, 1000000):
    current = i
    hops = 1
    while True: 
        if current in chains:
            chains[i] = chains[current] + hops 
            if bestVal < chains[i]:
                bestVal = chains[i]
                bestNum = i
            break
        elif current % 2 == 0:
            current /= 2 
        else:
            current = 3 * current + 1
        hops += 1

print(bestNum)

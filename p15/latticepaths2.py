#!/usr/bin/python

# magic formula: the number of paths from a given point is the sum of the two other points.
# at the ends, you only have 1. So start from the "end" being (0, 0) and left 1 is (1, 0)
# up one is (0, 1)

limit = 20
# map between coordinates and number of different paths from that coordinate
dictionary = {}

for i in range(limit + 1):
    for j in range(i + 1): 
        print("i " + str(i) + " j " + str(j))
        if i == 0 and j == 0:
            dictionary[i, j] = 0
        elif i == 0 or j == 0:
            dictionary[i, j] = 1
            dictionary[j, i] = 1
        else:
            value = dictionary[i - 1, j] + dictionary[i, j - 1]
            dictionary[i, j] = value
            dictionary[j, i] = value

print(dictionary[limit, limit])

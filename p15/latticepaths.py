#!/usr/bin/python
from collections import deque

paths = deque([[0, 0]]) 

limit = 20
numPaths = 0
while paths:
    path = paths.popleft()
    path1 = list(path)
    path2 = list(path)
    # once you hit your limit, you're done! only one way to go!
    if path[0] == limit or path[1] == limit: 
        numPaths += 1
        print(numPaths)
        continue
    path1[0] += 1
    paths.append(path1)
    path2[1] += 1
    paths.append(path2) 

#print(numPaths)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    cost = 0
    prev =0
    tf = k
    n = len(c)-1
    while n>=0:
        if k==0:
            if len(c)/tf >1:
                k=tf
            else:
                k=len(c)%tf
            prev+=1
        cost+=(prev+1)*c[n]
        k-=1
        n-=1
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

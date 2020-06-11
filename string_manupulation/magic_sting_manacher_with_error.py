#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    newS = ['#']
    for i in range(len(s)):
        newS += [s[i],'#'] 
    p = [0]*(len(newS))
    l=-1
    r=0
    for i in range(len(newS)):
        k = 0
        if i>r:
            k=1
        else:
            j = l+r-i
            k = min(p[j],r-i)
        while i-k>=0 and i+k < n and newS[i-k] == newS[i+1]:
            k+=1
        if newS[i-k] is not newS[i+k]:
            k-=1
        p[i]=k
        if i+k>r:
            l=i-k
            r=i+k
    count = 0
    for i in range(len(p)):
        print(p[i],len(newS))
        if p[i] is not 0:
            count=count+1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

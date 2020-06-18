#!/bin/python3

import math
import os
import random
import re
import sys


def commonChild(s1, s2):


    (m, n) = (len(s1), len(s2))
    M = [0 for x in range(m + 2)]
    count=0
    for i in range(1,m+1):
        prev  = 0
        for j in range(1,n+1):
            temp = M[j]
            if s1[i-1]==s2[j-1]:
                M[j]=prev+1
            else:
                M[j]=max(M[j],M[j-1])
            prev = temp

    return M[n]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
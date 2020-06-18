#!/bin/python3

import math
import os
import random
import re
import sys

def commonChild(s1, s2):


    (m, n) = (len(s1), len(s2))
    M = [[0 for x in range(n + 1)] for y in range(m + 1)]
    count=0
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 or j==0:
                M[i][j]=0
            elif s1[i-1]==s2[j-1]:
                M[i][j]=M[i-1][j-1]+1
            else:
                M[i][j]=max(M[i-1][j],M[i][j-1])

    return M[m][n]
    
if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)
    print(result)
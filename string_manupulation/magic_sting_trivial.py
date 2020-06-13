#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    
    d1=[0]*n
    d2=[0]*n
    for i in range(len(s)):
        d1[i]=1
        while 0<= i-d1[i] and i+d1[i]<n and s[i-d1[i]] is s[i+d1[i]]:
            d1[i]+=1
        d2[i]=0
        while 0<= i-d2[i]-1 and i+d2[i]<n and s[i-d2[i]-1] is s[i+d2[i]]:
            d2[i]+=1
    print(d2,d1)
    tot = sum(d1)+sum(d2)
    return tot



if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)


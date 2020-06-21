#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def Merge(a,b):
    d = []
    while len(a)>0 and len(b)>0:
        f_a = a[0][0]
        f_b = b[0][0]
        if f_a <= f_b:
            d.append(a[0])
            a = a[1:]
        else:
            d.append(b[0])
            b = b[1:]
    d = d + a + b
    return d

def MergeSort(contests):
    if len(contests)==0 or len(contests)==1:
        return contests
    mid  = int(len(contests)/2)
    a = MergeSort(contests[:mid])
    b = MergeSort(contests[mid:])
    c = Merge(a,b)
    return c


def luckBalance(k, contests):
    luck_balance = 0
    contests = MergeSort(contests)
    one_wala = []
    for i in range(len(contests)):
        if contests[i][1] == 1:
            one_wala.append(contests[i])
        elif contests[i][1] == 0:
            luck_balance+=contests[i][0]
    for i in range(len(one_wala)-1,-1,-1):
        if k>0:
            k-=1
            luck_balance+=one_wala[i][0]
        elif k==0:
            luck_balance-=one_wala[i][0]
    return luck_balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

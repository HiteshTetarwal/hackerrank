#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def Merge(a1,a2):
    d = []
    while len(a1)>0 and len(a2)>0:
        f_a1 = a1[0]
        f_a2 = a2[0]
        if f_a1<=f_a2:
            d.append(f_a1)
            a1=a1[1:]
        else:
            d.append(f_a2)
            a2=a2[1:]
    d = d + a1 + a2
    return d



def MergeSort(arr):
    if len(arr)>1:
        mid = int(len(arr)/2)
        a1 = MergeSort(arr[:mid])
        a2 = MergeSort(arr[mid:])
        AF = Merge(a1,a2)
        return AF
    else:
        return arr

def maximumToys(prices, k):
    sortedP = MergeSort(prices)
    print(sortedP)
    total = 0
    count = 0
    for i in range(len(sortedP)):
        total = total + sortedP[i]
        if total <= k:
            count = count + 1
        else:
            break
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

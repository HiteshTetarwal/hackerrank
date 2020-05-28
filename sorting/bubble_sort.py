#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


def countSwaps(a):
    count=0
    i=0
    while i<(len(a)-1):
        j=0
        while j<(len(a)-i-1):
            if a[j]>a[j+1]:
                x,y = swap(a[j],a[j+1])
                a[j]    = x
                a[j+1]  = y
                count=count+1
            j=j+1
        i = i+1
        if j == 0:
            break

    print("Array is sorted in",count,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    return
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
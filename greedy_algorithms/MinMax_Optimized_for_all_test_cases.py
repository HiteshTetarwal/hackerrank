#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arrS):
    arrS.sort()
    i=0
    unfairnessMin = 99999999
    while i<=len(arrS)-k:
        j = i+k
        diff = arrS[j-1]-arrS[i]
        if diff<unfairnessMin:
            unfairnessMin = diff
        i+=1
    return unfairnessMin

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

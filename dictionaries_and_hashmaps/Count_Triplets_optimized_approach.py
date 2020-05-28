#!/bin/python3
#this function return the correct solution to the count-tripplets on hacker rank but results in timelimit error
import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, g):
    count=0
    for i in range(len(arr)):
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

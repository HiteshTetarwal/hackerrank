#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the isValid function below.
def isValid(s):
    fd=defaultdict(int)
    freq=defaultdict(int)
    for i in s:
        fd[i]+=1
    min_count = 9999999
    max_count = 0
    for value in fd.values():
        freq[value]+=1
        if value < min_count:
            min_count = value
        if value > max_count:
            max_count = value

    if len(freq)==1:
        return "YES"
    elif len(freq)==2:
        if freq[max_count] == 1 and max_count - min_count == 1:
            return 'YES'
        elif freq[min_count] == 1 and min_count == 1:
            return 'YES'
    return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

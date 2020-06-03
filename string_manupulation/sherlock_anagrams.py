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
    count = 0
    for value in fd.values():
        freq[value]+=1

    if len(freq)==1:
        return "YES"
    elif len(freq)==2:
        i=0
        for value in freq.values():
            if i==0:
                if value==1:
                    return "YES"
            elif i==1:
                if value==1:
                    return "YES"
                else:
                    return "NO"
            i+=1
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

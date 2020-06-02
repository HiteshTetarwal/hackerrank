#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    da = {}
    db = {}
    count = 0
    for i in range(len(a)):
        if a[i] not in da:
            da[a[i]] = 1
        else:
            da[a[i]] += 1
    for i in range(len(b)):
        if b[i] not in db:
            db[b[i]] = 1
        else:
            db[b[i]] += 1
    for key,values in da.items():
        if key in db:
            count = count + abs(da[key]-db[key])
            db.pop(key)
        elif key not in db:
            count=count+values
    for key,value in db.items():
        count+=value
        
    return count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = dict()
    ans = ""
    for x in queries:
        if x[0]==1:
            if x[1] not in  freq:
                freq[x[1]]=1
            else:
                freq[x[1]]+=1
        if x[0]==2:
            if x[1] in freq:
                freq[x[1]]-=1
            else:
                continue
        if x[0]==3:
            if x[1] in freq.values():
                ans += "1"
            else:
                ans += "0"

    return ans




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

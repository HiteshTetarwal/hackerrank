#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    ana=0
    temp={}        
    for i in range(len(s)):
        for j in range(i,len(s)):
            subs=''.join(sorted(s[i:j+1])) #sorted the substring and joined to a single string
            if subs not in temp:#add the substring in temp dictionary as a key and make sure that the count of each substring is kept the value
                temp[subs]=1
            else:
                temp[subs]+=1
            ana+=temp[subs]-1 #subtract one from the value so that single count substrings are not considered 
    return ana


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

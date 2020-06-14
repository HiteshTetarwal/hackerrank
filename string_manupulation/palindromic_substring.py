#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def checkevenpalindrome(s):
    i = 0
    j=len(s)-1
    status = True
    while i<j:
        if s[i]==s[j]:
            pass
        else:
            return False
        i+=1
        j-=1
    return status

def checkoddpalindrome(s):
    i = 0
    j=len(s)-1
    status =True
    while i!=j:
        if s[i]==s[j]:
            pass
        else:
            return False
        i+=1
        j-=1
    return status



def substrCount(n, s):
    sub = []
    count=0
    for i in range(n):
        temp=''
        for j in range(i,n):
            temp+=s[j]
            # print(temp)
            if len(temp)&1:
                if checkevenpalindrome(temp):
                    print(temp)
                    count+=1
            else:
                if len(temp)==1:
                    print(temp)
                    count+=1
                elif checkoddpalindrome(temp):
                    print(temp)
                    count+=1
    return count
    # for key in sub:
    #     if (len(key))&1:
    #         if checkevenpalindrome(key):
    #             count+=1
    #     else:
    #         if checkoddpalindrome(key):
    #             count+=1
if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)


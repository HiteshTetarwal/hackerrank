#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # print(cost,money)
    one = 0
    two = 0
    temp2 = []
    for i in range(len(cost)):
        temp1 = cost[i]
        temp2 = money - temp1
        one = i+1
        flag = False
        for j in range(i+1,len(cost)):
            if cost[j] == temp2:
                two = j+1
                flag = True
                break
        if flag == True:
            break
    print(one,two) 

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

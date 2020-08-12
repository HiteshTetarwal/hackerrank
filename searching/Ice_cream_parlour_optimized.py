#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_flavour = {}
    for i,icost in enumerate(cost):
        if money-icost in cost_flavour:
            print(cost_flavour[money-icost]+1,i+1)
            return
        else:
            cost_flavour[icost] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

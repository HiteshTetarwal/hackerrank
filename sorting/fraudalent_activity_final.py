#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.

def get_median(counting_sort_list,trailing_days,median_position):
    counter,left = 0,0
    while counter<median_position:
        counter += counting_sort_list[left]
        left+=1

    right =left
    left -=1

    if counter > median_position or trailing_days %2 != 0:
        return left
    else:
        while counting_sort_list[right] == 0:
            right+=1
        return (left+right)/2




def activityNotifications(expenditure, trailing_days):
    counting_sort_list = [0]*201
    end = trailing_days


    for i in range(0,end):
        counting_sort_list[expenditure[i]]+=1
    current = 0
    total_notifications=0


    if trailing_days%2==0:
        median_position = int(trailing_days/2)
    else:
        median_position = int(trailing_days/2)+1

    total_expenditure_length = len(expenditure)

    while end<total_expenditure_length:
        median = get_median(counting_sort_list,trailing_days,median_position)

        if expenditure[end] >= median*2:
            total_notifications+=1

        counting_sort_list[expenditure[current]] -= 1
        counting_sort_list[expenditure[end]]      +=    1

        current += 1
        end     += 1

    return total_notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

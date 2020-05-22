#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    checker_note={}
    checker_magazine={}
    found =  False
    for i in range(len(note)):
        if note[i] not in checker_note:
            checker_note[note[i]]=1
            continue
        checker_note[note[i]]+=1
    for i in range(len(magazine)):
        if magazine[i] in checker_note and magazine[i] not in checker_magazine:
            checker_magazine[magazine[i]]=1
            continue
        elif magazine[i] in checker_note and magazine[i] in checker_magazine:
            checker_magazine[magazine[i]]+=1
    if checker_magazine==checker_note:
        print("Yes")
    elif checker_note.keys() == checker_magazine.keys():
        for key in checker_note.keys():
            if checker_note[key] <= checker_magazine[key]:
                continue
            else:
                print("No")
                found = True
                break
        if found == False:
            print("Yes")
    else:
        print("No")
            
    return

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

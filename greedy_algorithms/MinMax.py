    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    # Complete the maxMin function below.

    def Merge(a1,a2):
        d = []
        a = a1
        b = a2
        while len(a)>0 and len(b)>0:
            if a[0]<=b[0]:
                d.append(a[0])
                a = a[1:]
            else:
                d.append(b[0])
                b = b[1:]
        d = d + a + b
        return d


    def MergeSort(arr):
        if len(arr)==1 or len(arr)==0:
            return arr
        mid = int(len(arr)/2)
        a = MergeSort(arr[:mid])
        b = MergeSort(arr[mid:])
        c = Merge(a,b)

        return c


    def maxMin(k, arr):
        arrS = MergeSort(arr)
        i=0
        unfairnessMin = 99999999
        while i<=len(arrS)-k:
            j = i+k
            diff = max(arrS[i:j])-min(arrS[i:j])
            if diff<unfairnessMin:
                unfairnessMin = diff
            i+=1
        return unfairnessMin
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        k = int(input())

        arr = []

        for _ in range(n):
            arr_item = int(input())
            arr.append(arr_item)

        result = maxMin(k, arr)

        print(result)

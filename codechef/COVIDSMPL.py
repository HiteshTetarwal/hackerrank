import random
import sys
n = int(input())
while n:
    n-=1
    count=0
    N=list(map(int, input().split()))
    M = []
    for i in range(0,N[0]):
        a=[]
        for j in range(0,N[0]):
            print(1,i+1,j+1,i+1,j+1)
            sys.stdout.flush()
            take_1 = int(input())
            if take_1 == 1:
                a.append(1)
            else:
                a.append(0)
        M.append(a)
    print(2)
    for i in range(N[0]): 
        for j in range(N[0]): 
            print(M[i][j], end = " ") 
        print()
    sys.stdout.flush()
    right = int(input())
    if right == 1 :
        continue
    else:
        break
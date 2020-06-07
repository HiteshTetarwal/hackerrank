# cook your dish here

def printascending(x,y):
    for i in range(x,y):
        print(i,' ',end='')

def printdescending(x,y):
    for i in range(y-1,x-1,-1):
        print(i,' ',end='')

def delicious_matrix(n):
    x=1
    i=1
    while i<=n:
        if i%2!=0:
            y=x+n
            printascending(x,y)
            print(end='\n')
        elif i%2==0:
            y=x+n
            printdescending(x,y)
            print(end='\n')
        x=x+n
        i+=1

if __name__ == '__main__':


    q = int(input())
    for q_itr in range(q):
        n = int(input())
        delicious_matrix(n)
# cook your dish here
def getcost(n):
    tot=0
    for i in range(1,n+1):
        cost=0
        print(i)
        minimum=9999
        for j in range(i+1,n+1):
            if i^j<=minimum and i^j>0:
                minimum= i^j
                cost = i^j
        tot+=cost        
    return tot
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = int(input())
        result = getcost(s)
        print(result)
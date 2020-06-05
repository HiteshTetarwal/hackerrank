# cook your dish here
def loss(price,k):
    loss = 0
    for i in range(len(price)):
        if price[i]>=k:
            loss+=price[i]-k
            
    return loss
    
if __name__ == '__main__':


    q = int(input())
    for q_itr in range(q):
        s =  list(map(int, input().split()))
        arr = list(map(int, input().split()))
        result = loss(arr,s[1])
        print(result)
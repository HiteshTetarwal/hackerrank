from collections import defaultdict
def can_change(people):
    stack = defaultdict(int)
    
    for i in range(len(people)):
        if people[i]==5:
            stack[people[i]]+=1
        elif people[i]==15:
            if stack[10]>=1:
                stack[10]-=1
                stack[people[i]]+=1
            elif stack[5]>=2:
                stack[5]-=2
                stack[people[i]]+=1
            else:
                return 'NO'
        elif people[i]==10:
            if stack[5]>=1:
                stack[5]-=1
                stack[people[i]]+=1
            else:
                return 'NO'


    return 'YES'


if __name__ == '__main__':


    q = int(input())
    for q_itr in range(q):
        s =  int(input())
        arr = list(map(int, input().split()))
        result = can_change(arr)
        print(result)
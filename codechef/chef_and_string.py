def is_pair(s):
    count = 0
    i=0
    while i<len(s)-1:
        if s[i] == 'x' and s[i+1]=='y':
            count=count+1
            i=i+1
        elif s[i]=='y' and s[i+1]=='x':
            count =count+1
            i+=1
            
        i+=1
    return count


if __name__ == '__main__':


    q = int(input())
    for q_itr in range(q):
        s=input()
        result = is_pair(s)
        print(result)   
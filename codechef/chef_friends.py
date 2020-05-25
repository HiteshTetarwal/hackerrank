# cook your dish here
def canretrieve(s):
    substings={}
    count=0
    len_1=int(len(s)/2)
    if len_1%2 == 0:
        len__1=int(len_1/2)
        len__2=len__1
    else:
        len__1=int(len_1/2)
        len__2=len_1-len__1
        
    for i in range(len(s)):
        temp=''
        for j in range(i+1,len(s)):
            temp = ''.join(s[i:j+1])
            if len__1 == 1:
                return 0
            if temp not in substings and (len(temp)==len__1 or len(temp)==len__2):
                substings[temp] = 1
            elif temp not in substings and (len(temp)==len__1 or len(temp)==len__2):
                substings[temp] += 1
            print(substings,len__1,len__2)
            if count>1:
                return 1
            if substings[temp]>1:
                count=count+1
            
    return 0

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = canretrieve(s)
        print(result)   
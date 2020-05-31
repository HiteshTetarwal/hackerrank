# def getNumberOfIntegers(L, R, K):
#     i=int(L)
#     nonzer=[1,2,3,4,5,6,7,8,9,0]
#     count=0
#     while i<=int(R):
#         x=str(i)
#         if '0' not in x and len(x)==K:
#             count=count+1

#         for j in range(len(x)):
#             new_i=''
#             if x[j]=='0':
#                 new_i = x[:j]+x[j+1:]
#         print(i,new_i)
#         if len(new_i)==K:
#             count=count+1
#         i=i+1
#     return count







def getNumberOfIntegers(L, R, K):
    i=int(L)+1
    count=0
    withzero=[]
    while i<=int(R):
        x=str(i)
        if '0' not in x and len(x)==K:
            print(x)
            count=count+1
        if '0' in x:
            withzero.append(x)
        i=i+1
    for i in range(len(withzero)):
        l = withzero[i].count('0')
        new_l = len(withzero[i])-l
        print(new_l,len(withzero[i]),withzero[i],l)
        if new_l == K:
            count = count+1
    return count

print(getNumberOfIntegers('2','15',1))
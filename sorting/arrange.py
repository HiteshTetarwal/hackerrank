
def arrangeStudents(a, b):

    empty=[[999999,'x']]
    i=0
    j=0
    if len(a)!=len(b):
        return 'NO'
    while i<=len(a)-1 and j<=len(a)-1:
        if a[i]<b[j]:
            if empty[-1][1]=='b':
                return 'NO'
            empty.append([a[i],'b'])
            i=i+1
        elif b[j]<a[i]:
            if empty[-1][1]=='g':
                return 'NO'
            empty.append([b[j],'g'])
            j=j+1
        elif a[i]==b[j]:
            if empty[-1][1]=='g':
                empty.append([a[j],'b'])
                empty.append([b[j],'g'])
            if empty[-1][1]=='b':
                empty.append([b[j],'g'])
                empty.append([a[j],'b'])
            i=i+1
            j=j+1
    if len(empty)!=2*len(a)+1:
         if i<j:
            if empty[-1][1]=='g':
               if a[i]>=empty[-1][0]:
                   empty.append([a[i],'b'])
               	   print(empty)
                   return 'YES'
               else:
                   return 'NO'
            else:
                return 'NO'
         elif j<i:
            if empty[-1][1]=='b':
               if b[j]>=empty[-1][0]:
                   empty.append([b[j],'g'])
               	   print(empty)
                   return 'YES'
               else:
                   return 'NO'
            else:
                return 'NO'
    print(empty)
    return 'YES'

print(arrangeStudents([2,3,5],[1,3,4]))
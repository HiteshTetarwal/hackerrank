def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    stack=[-99999]
    for i in range(0,len(queries)): 
        print(i)
        arr[queries[i][0]-1] += queries[i][2]
        if queries[i][1] < len(arr)-1:
            arr[queries[i][1]] -= queries[i][2]
        print(arr)

    j=1
    while j<n:
        arr[j] += arr[j-1]
        if stack[-1]<arr[j]:
            stack.append(arr[j])
        print(arr)
        j=j+1

    return stack[-1]
        
    
#old approach


    # i = queries[0][0]-1
    # ql = 0
    # j=0
    # stack=[-99999]
    # while i>=queries[j][0]-1 and i<=queries[j][1]-1:
    #     added[i]=added[i]+queries[j][2]
    #     if added[i]>stack[-1]:
    #         stack.append(added[i])
    #     if i == queries[j][1]-1:
    #         ql = ql+1
    #         if ql > len(queries)-1:
    #             break
    #         j=j+1
    #         i=queries[j][0]-1
    #         continue
    #     i=i+1
        
    # return stack[-1]

val = arrayManipulation(4,[[2,3,603], [1, 1, 286], [4, 4, 882]])


# val = arrayManipulation(10,[[2,6,8], [3, 5, 7], [1, 8, 1],[5,9,15]])
print(val)
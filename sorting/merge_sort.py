def Merge(a1,a2):
    print(a1,a2)
    d = []
    while len(a1)>0 and len(a2)>0:
        f_a1 = a1[0]
        f_a2 = a2[0]
        if f_a1<=f_a2:
            d.append(f_a1)
            a1=a1[1:]
        else:
            d.append(f_a2)
            a2=a2[1:]
    d = d + a1 + a2
    return d



def MergeSort(arr):
    if len(arr)>1:
        mid = int(len(arr)/2)
        a1 = MergeSort(arr[:mid])
        a2 = MergeSort(arr[mid:])
        AF = Merge(a1,a2)
        return AF
    else:
        return arr

print(MergeSort([5,6,4,7,9,1,6,4,2]))
def Merge(a1,a2):
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

def activityNotifications(expenditure, d):
    i=0
    count = 0
    while i<len(expenditure)-d-1:
        trail = MergeSort(expenditure[i:i+d])
        if d%2 == 0:
            mid     = int(d/2)
            mid2    = mid+1
            median  = int((trail[mid]+trail[mid2])/2)
        elif d%2 !=0:
            mid     = int(d/2)
            median  = int(trail[mid])
        if expenditure[i+d]>=(2*median):
            count=count+1            
        i+=1
    return count




print([1,2,6,4,8,,6,,8,5,6,4,8,9],5)
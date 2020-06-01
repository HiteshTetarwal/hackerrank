def MergeSort(arr):
    if len(arr)==1:
        return arr,0
    else:
        mid = int(len(arr)/2)
        a,a1 = MergeSort(arr[:mid])
        b,b1 = MergeSort(arr[mid:])

        d = []
        i=0
        j=0
        count = 0+a1+b1
        while len(a)>0 and len(b)>0:
            f_a = a[0]
            f_b = b[0]
            if f_a <= f_b:
                d.append(f_a)
                a = a[1:]
                i+=1
            else:
                d.append(f_b)
                b = b[1:]
                j+=1
                count = count+len(a)-i
        d = d + a + b
        return d,count

# def countInversions(arr):



print(MergeSort([1,1,1,2,2]))
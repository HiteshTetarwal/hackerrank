# def binary_search(arr,low,high,key):
# 	if high<low:
# 		return low-1
# 	mid = int(low + (high-low)/2)
# 	if key==arr[mid]:
# 		return mid
# 	elif key<arr[mid]:
# 		return binary_search(arr,low,mid-1,key)
# 	else:
# 		return binary_search(arr,mid+1,high,key)


# if __name__ == '__main__':
#     input_numbers = [int(x) for x in input().split()]
#     high = int(input())
#     low  = int(input())
#     key  = int(input())
#     print(binary_search(input_numbers))


# python3
seq = [int(i) for i in input().split()]
search_seq = [int(i) for i in input().split()]
n = seq[0]
seq = seq[1:]

def binary_search(seq, elt, r):
    l = 0
    while l<=r: 
        m = (l+r)//2
        if elt > seq[m]:
            l = m + 1
        elif elt < seq[m]:
            r = m - 1
        else:
            return m
    return -1

soln = list()
for i in search_seq[1:]:
    ans = binary_search(seq, i, n-1)
    soln.append(ans)
print(' '.join([str(i) for i in soln]))
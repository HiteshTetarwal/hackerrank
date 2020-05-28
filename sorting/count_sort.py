def CountSort(arr):
	count = [0]*(len(arr)+1)
	for i in range(len(arr)):
		count[arr[i]]=count[arr[i]]+1

	pos = [0]*len(count)
	pos[0] = 1

	for j in range(1,len(pos)):
		pos[j] = pos[j-1] + count[j-1]
	sort = [0]*(len(arr)+1)
	for i in range(len(arr)):
		sort[pos[i]] = arr[i]
		pos[arr[i]] = pos[arr[i]]+1

	return sort

print(CountSort([5,6,4,7,9,1,6,4,2]))

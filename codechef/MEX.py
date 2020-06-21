def get_index(n,arr):
	for i in range(len(arr)):
		if arr[i]==(n):
			return i

def MEX(nbm,m_arr):
	n = nbm[0]
	m = nbm[1]
	current =0
	last = 0
	nextmiss = 0
	if m-1 not in m_arr:
		return -1
	else:
		index_left = get_index(m-1,m_arr)
		z = m-1
		while m_arr[index_left]==z:
			index_left-=1
			z-=1
		index_left+=1
		mex = len(m_arr)-index_left

	return mex

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        nbm = list(map(int, input().split()))
        m_arr = list(map(int, input().split()))
        result = MEX(nbm,m_arr)
        print(result)
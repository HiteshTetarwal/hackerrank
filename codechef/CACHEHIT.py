def MEX(nbm,m_arr):
	count=0
	n = nbm[0]
	b = nbm[1]
	m = nbm[2]
	M = m_arr
	visited_blocks = dict()
	recents = ['abc']
	for i in range(len(M)):
		if int(M[i]/b) == 0:
			get_block = 0
		else:
			get_block = int(M[i]/b)
		block = str(get_block)
		if block == recents[-1]:
			continue
		recents.append(block)
		count+=1
		# # print(block,n,M[i])
		# if block not in visited_blocks:
		# 	visited_blocks[block]=1
		# 	count+=1
		# else:
		# 	continue
	return count

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        nbm = list(map(int, input().split()))
        m_arr = list(map(int, input().split()))
        result = cachehit(nbm,m_arr)
        print(result)
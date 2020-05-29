def minimumMoves(s, d):
    i=0
    swap=0
    alpha = [char for char in s]
    print(alpha)
    j=0
    while j<=len(alpha)-1:
    	if len(alpha[j:j+d])<d:
    		break
    	if '1' not in alpha[j:j+d]:
    		alpha[j+d-1]='1'
    		swap=swap+1

    	j=j+1
    print(alpha)
    return swap




print(minimumMoves('101',2))
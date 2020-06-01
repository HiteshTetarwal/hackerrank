def WierdAlgorithm(n):
	while(True):
		if n%2==0:
			n=n/2
			if n==1:
				return n
			print(n, end =" ")

		else:
			n=(3*n)+1
			print(n, end =" ")

n = int(input())
print(WierdAlgorithm(n))
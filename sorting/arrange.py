def arrangeStudents(a, b):

	if a[0]>b[0]:
		temp=b
		b=a
		a=b
	i=0
	j=0
	flag = True
	previous =  ''

	while i<len(a)-1:
		if a[i]==a[j] and i>0:
			if previous == 'i':
				return 'NO'
			continue
		if a[i]<=b[j]:
			i=i+1
			previous = 'i'
			if a[i]<=b[j]:
				return 'NO'
		elif a[i]>b[j]:
			j=j+1
			previous = 'j'
			if a[i]>a[i]:
				return 'NO'
	return 'YES'

print(arrangeStudents([1,2,5],[2,3,6]))
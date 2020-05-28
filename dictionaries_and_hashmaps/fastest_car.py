def MaxProduct(arr):
	products = []
	for i in range(len(arr)):
		mul = arr[i]
		for j in range(i+1,len(arr)):
			mul = mul*arr[j]
		products.append(mul)
	stack = [-9999]
	print(products)
	for i in range(0,len(products)):
		if products[i]>stack[-1]:
			stack.append(products[i])
	print(stack)
	return stack[-1]


result=MaxProduct([2,0,-3,8,-4,-9])
print(result)
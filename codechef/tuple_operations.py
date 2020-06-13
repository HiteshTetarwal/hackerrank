# def is_even_diff(initial,final):
# 	diff = []
# 	for i in range(len(initial)):
# 		if (final[i]-initial[i])!=0:
# 			diff.append(final[i]-initial[i])
# 	try:
# 		first = diff[0]
# 	except:
# 		return False

# 	for i in range(1,len(diff)):
# 		if first is diff[i]:
# 			continue
# 		else:
# 			return False
# 	return False

# def is_even_div(initial,final):
# 	diff = []
# 	for i in range(len(initial)):
# 		if (final[i]/initial[i])!=1:
# 			diff.append(final[i]/initial[i])
# 	try:
# 		first = diff[0]
# 	except:
# 		return False

# 	for i in range(1,len(diff)):
# 		if first is diff[i]:
# 			continue
# 		else:
# 			return False
# 	return False

# def operations(initial,final):
	# count=0
	# if is_even_diff(initial,final):
	# 	return 1

	# if is_even_div(initial,final):
	# 	return 1
	# while initial!=final:
	# 	take_divisors = []
	# 	for i in range(len(initial)):
	# 		take_divisors.append(final[i]/initial[i])
	# 	print(1)

	# 	mini = 9999
	# 	for i in range(len(take_divisors)):
	# 		if take_divisors[i].is_integer() and (final[i]/initial[i]) != 1:
	# 			if take_divisors[i]<mini:
	# 				mini = take_divisors[i]
	# 	print(2)
	# 	previous = count
	# 	for i in range(len(initial)):
	# 		if (take_divisors[i]).is_integer() and (take_divisors[i]) != 1:
	# 			initial[i]=initial[i]*mini
	# 			count=previous+1
	# 	print(3)
	# 	if initial == final:
	# 		break


	# 	take_diff = []
	# 	new_p = count
	# 	for i in range(len(initial)):
	# 		take_diff.append(final[i]-initial[i])
	# 	print(4)
	# 	mini_diff = 9999
	# 	for i in range(len(take_diff)):
	# 		if take_diff[i]<mini_diff and take_diff[i]>0:
	# 			mini_diff = take_diff[i]
	# 	print(5)
	# 	for i in range(len(initial)):
	# 		if take_diff[i]==0:
	# 			continue
	# 		else:
	# 			initial[i]=initial[i]+mini_diff
	# 			count = new_p +1
	# 	print(6)
	# return count



def operations(initial,final):
	while initial!=final:
		for i in range(len(initial)):
			

if __name__ == '__main__':


    q = int(input())
    for q_itr in range(q):
        initial	 = list(map(int, input().split()))
        final	 = list(map(int, input().split()))
        result = operations(initial,final)
        print(result)
test =int(input())
# test = 1
import math
def bin_trail_zeroes(s):
	return len(s) - len(s.rstrip('0'))
while test :
	test -= 1
	tom = int(input())
	# tom = 28
	# tom = 11
	#trailing zeroes
	bin_tom = bin(tom)[2:]
	tz = bin_trail_zeroes(bin_tom)
	orig_len = len(bin_tom)
	ones_after_tz = 0
	ans = 0
	# print(bin_tom)
	for i in range(orig_len-1-tz,0,-1):
		if bin_tom[i] == '1':
			ans += 1

	cnt = orig_len
	cnt -= 1
	while cnt>0:
		combi = cnt - 1 - tz
		
		if combi > 0:
			ans += 1 #for eg - 000 when there is no 1

			#fix a zero
			for i in range(1,combi+1):

				remaining_places = combi-i #fixed i zeroes, for eg - 1 in first iteration
				for j in range(1,remaining_places+1):

					ans += math.comb(remaining_places,j)
		cnt -= 1


	print(ans)
	# print(tz,orig_len,ans)
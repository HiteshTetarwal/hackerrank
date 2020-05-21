# python3


def max_pairwise_product(nums):
    index1=-1
    #find the maximum
    for i in range(len(nums)):
        # index1=i
        if(nums[i]>nums[index1] or index1 == -1):
            index1=i
    # return index1
    index2=-1
    for j in range(len(nums)):
        if((j!=index1) or (nums[j]>nums[index2]) and (index2==-1) ):
            index2=j
    # print(index1,index2)

    return nums[index1]*nums[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))




# """class Solution:
# 	def MaxPairwiseProduct(self, nums):
# 		mul=0
# 		max_new=0
# 		for i in range(0,len(nums)):
# 			for j in range(i+1,len(nums)):
# 				mul_before=mul
# 				mul=nums[i]*nums[j]
# 				if mul<mul_before:
# 					mul=mul_before
			
# 			if max_new<=mul:
# 				max_new=mul
# 		return max_new
# """

# class Solution2(object):
# 	def MaxPairwiseProductFast(self,nums):
# 		index1=-1
# 		#find the maximum
# 		for i in range(len(nums)):
# 			# index1=i
# 			if(nums[i]>nums[index1] or index1 == -1):
# 				index1=i
# 		# return index1
# 		index2=-1
# 		for j in range(len(nums)):
# 			if(((j!=index1) or (index2==-1)) or nums[j]>nums[index2]):
# 				index2=j

# 		return nums[index1]*nums[index2]
# 		#find second maximum	

# if __name__=="__main__":
# 	lst = [ ] 
# 	n = int(input("Enter number of elements : ")) 
	  
# 	for i in range(0, n): 
# 	    ele = [input(), int(input())] 
# 	    lst.append(ele) 
# 	obj1=Solution2()
# 	print(obj1.MaxPairwiseProductFast(lst))



# # find two indices such that there values are the largest and second largest
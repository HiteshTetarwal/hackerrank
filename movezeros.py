

class Solution:
    def moveZeroes(self, nums):
        count=0
        count_zero=nums.count(0)
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[count]=nums[i]
                count=count+1
        while count_zero>0:
            nums[-count_zero]=0
            count_zero=count_zero-1
        return nums


if __name__=="__main__":
    arr = [0,1,0,3,12] 
    print(arr)
    n = len(arr)
    obj1=Solution()
    print(obj1.moveZeroes(arr))



"""
solution1

class Solution:
    def moveZeroes(self, nums):
        
        def swap(num1,num2):
            temp=num1
            num1=num2
            num2=temp
            return num1,num2
        times=len(nums)**2
        n=len(nums)
        # print(n)
        j=0
        def arranger(nums,times,j):
                for i in range(0,len(nums)-1):
                    print(i)
                    if nums[i]==0:
                        nums[i],nums[i+1]=swap(nums[i],nums[i+1])
                # print(len(nums))
                j=j+len(nums)
                print(j,times)
                # print(nums)
                if j<times:
                    arranger(nums,times,j)
        arranger(nums,times,j) 

        return nums
"""


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
        
#         def swap(num1,num2):
#             temp=num1
#             num1=num2
#             num2=num1
#             return num1,num2
        
#         for i in range(0,len(nums)):
#             j=i
#             if nums[i]==0:
#                 temp=nums[i]
#                 while(j<=len(nums)-1):
#                     if j<(len(nums)-1):
#                         nums[j],nums[j+1]=swap(nums[j],nums[j+1])
#                     j=j+1
#                     if j<(len(nums)-1) and nums[j]==0:
#                         continue
#                         

# class Solution:
#     def moveZeroes(self, nums):
        
#         def swap(num1,num2):
#             temp=num1
#             num1=num2
#             num2=temp
#             return num1,num2
#         j=len(nums)
#         while j>0:
#             for i in range(0,len(nums)):
#                 if nums[i]==0 and (i+1)<len(nums):
#                     nums[i],nums[i+1]=swap(nums[i],nums[i+1])
#             j=j-1
#                         
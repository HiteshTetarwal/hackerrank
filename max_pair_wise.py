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

    return nums[index1]*nums[index2]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

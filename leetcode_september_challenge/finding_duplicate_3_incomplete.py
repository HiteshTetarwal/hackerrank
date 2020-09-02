class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:   
        nums.sort()
        for i in range(len(nums)-1):
            j = i+1
            if abs(nums[i] - nums[i+1]) <= t and abs(i - (i+1)) <= k:
                return True
            else:
                for x in range(i+1,len(nums)):
                    if abs(nums[i] - nums[x]) <= t and abs(i - (x)) <= k:
                        return True
        return False
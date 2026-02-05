class Solution(object):
    def buildArray(self, nums):
        ans = [nums[nums[i]] for i in range(len(nums))] 
        return ans
        

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sortedNums = sorted(nums)
        ans = []
        for items in nums:
            ans.append(sortedNums.index(items))
        return ans
        

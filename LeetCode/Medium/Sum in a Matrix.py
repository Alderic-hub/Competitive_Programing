class Solution(object):
    def matrixSum(self, nums):
        length = len(nums[0]) -1
        ans = 0 
        nums = [sorted(num) for num in nums]
        while length >= 0:
            lis = []
            for num in nums:
                lis.append(num[length])
            ans+=max(lis)
            length -= 1
        return ans
        

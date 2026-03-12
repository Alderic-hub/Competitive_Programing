class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        end = len(nums)-1
        start = 0
        ans = 0
        while start < end:
            val = nums[start] + nums[end]
            if val < k:
                start += 1
            elif val > k:
                end -= 1
            else:
                start += 1
                end -= 1
                ans += 1
        return ans 

        

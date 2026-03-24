class Solution(object):
    def countGood(self, nums, k):
        n = len(nums)
        unique = {}
        start = 0
        pairs = 0
        ans = 0
        
        for i in range(n):
            x = nums[i]
            if x in unique:
                pairs += unique[x]
            unique[nums[i]] = unique.get(nums[i], 0) + 1
            
            while pairs >= k:
                ans += n - i
                y = nums[start]
                unique[y] -= 1
                pairs -= unique[y]
                start += 1
        
        return ans

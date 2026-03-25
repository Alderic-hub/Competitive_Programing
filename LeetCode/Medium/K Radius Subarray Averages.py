class Solution(object):
    def getAverages(self, nums, k):
        val = (k*2) + 1
        length = len(nums)
        ans = [-1] * length
        nums_new = list(nums)
        
        if k == 0:
            return nums
        
        for n in range(1, length):
            nums_new[n] += nums_new[n-1]
        
        for n in range(k, length - k):
            if n - k - 1 >= 0:
                answer = (nums_new[n+k] - nums_new[n-k-1]) // val
            else:
                answer = nums_new[n+k] // val
            
            ans[n] = answer
        
        return ans

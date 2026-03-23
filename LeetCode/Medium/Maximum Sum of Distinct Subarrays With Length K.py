class Solution(object):
    def maximumSubarraySum(self, nums, k):
        length = len(nums)
        ans = 0
        val = 0
        start = 0
        seen = set()
        for pointer in range(length):
            while nums[pointer] in seen or (pointer - start) == k:
                seen.remove(nums[start])
                val -= nums[start]
                start += 1
                
            seen.add(nums[pointer])
            val += nums[pointer]
            
            if (pointer - start + 1) == k:
                if val > ans:
                    ans = val
                    
        return ans

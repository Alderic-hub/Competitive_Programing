class Solution(object):
    def smallestDivisor(self, nums, threshold):
        start = 1
        end = max(nums)
        ans = end
        
        while start <= end:
            mid = (start + end) // 2
            value = 0
            for x in nums:
                value += (x + mid - 1) // mid
            if value <= threshold:
                ans = mid
                end = mid - 1   
            else:
                start = mid + 1

        return ans

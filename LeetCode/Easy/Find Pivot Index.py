class Solution(object):
    def pivotIndex(self, nums):
        start = 0
        end = len(nums)
        for n in range(end):
            high = sum(nums[:n])
            low = sum(nums[n+1:])
            if high == low:
                return n
        return -1

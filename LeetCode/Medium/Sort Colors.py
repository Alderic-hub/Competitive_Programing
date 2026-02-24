class Solution(object):
    def sortColors(self, nums):
        length = len(nums) - 1
        for n in range(length,0,-1):
            for y in range(n):
                if nums[y] > nums[y+1]:
                    nums[y] , nums[y+1] = nums[y+1] , nums[y]

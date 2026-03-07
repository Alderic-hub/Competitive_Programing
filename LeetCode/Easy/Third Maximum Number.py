class Solution(object):
    def thirdMax(self, nums):
        nums = sorted(set(nums))
        length = len(nums)
        if length < 3:
            return nums[-1]
        return nums[-3]


            

class Solution(object):
    def rotate(self, nums, k):
        end = len(nums) - k
        if abs(end) > len(nums):
            for _ in range(abs(end)):
                val = nums.pop()
                nums.insert(0,val)
        else:
            nums[:] = nums[end:] + nums[:end]

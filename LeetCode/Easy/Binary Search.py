class Solution(object):
    def search(self, nums, target):

        end = len(nums) -1
        start = 0

        while end >= start:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        return -1



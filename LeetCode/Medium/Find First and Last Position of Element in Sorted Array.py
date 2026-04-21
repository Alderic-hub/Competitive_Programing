class Solution(object):
    def searchRange(self, nums, target):

        end = len(nums) -1
        start = 0
        val = 0
        length = len(nums)
        truth = False
        while end >= start:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                val = mid
                truth = True
                break
        
        min = val
        max = val
        while min > 0 and nums[min-1] == target:
            min -=1
        while max < length-1 and nums[max+1] == target:
            max += 1
        answer = [min,max]
        if not min and not truth:
            answer = [-1,-1]
        return answer


        

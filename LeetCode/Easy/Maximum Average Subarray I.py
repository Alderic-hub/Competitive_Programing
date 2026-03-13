class Solution(object):
    def findMaxAverage(self, nums, k):
        length = len(nums)  +1
        start = 0
        end = k-1
        ans = None
        value = float(sum(nums[start:k]))
        for _ in range(length -k):
            val = value/k
            if not ans or ans < val:
                ans = val
            end += 1
            if end < length-1:
                print(nums[start],nums[end] )
                value = (value - nums[start] + nums[end])
            start += 1
            
        return ans


        

class Solution(object):
    def findTheWinner(self, n, k):
        nums = []
        for n in range(1, n+1):
            nums.append(n)
        val = len(nums)
        if val == 1:
            return nums[0]
        pointer = 0
        while val > 1:
            pointer += k -1
            while pointer >= val:
                pointer -= val
            nums.pop(pointer)
            val = len(nums)   
        return nums[0]
            

class Solution(object):
    def runningSum(self, nums):
        number = 0
        val = 0
        ans = []
        for n in nums:
            val += n
            ans.append(val)
        return ans

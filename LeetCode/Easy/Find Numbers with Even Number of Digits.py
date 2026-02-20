class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for items in nums:
            val = str(items)
            if len(val)%2 == 0:
                count += 1
        return count

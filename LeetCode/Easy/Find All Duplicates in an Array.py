class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        nums_dict = {}
        for num in nums:
            nums_dict[num]=nums_dict.get(num, 0) + 1
        for key, value in nums_dict.items():
            if value > 1:
                ans.append(key)
        return ans

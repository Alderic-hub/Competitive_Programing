class Solution(object):
    def sortColors(self, nums):
        rep1=nums.count(2)
        rep2 =nums.count(0)
        for i in range(rep1):
            nums.remove(2)
            nums.append(2)
        nums.reverse()
        for i in range(rep2):
            nums.remove(0)
            nums.append(0)
        nums.reverse()

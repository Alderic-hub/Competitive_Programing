class Solution(object):
    def targetIndices(self, nums, target):
        for n in range(len(nums), 0, -1):
            for y in range(n-1):
                if nums[y] > nums[y+1]:
                    nums[y+1] , nums[y] = nums[y], nums[y+1]
        ans = []
        if target not in nums:
            return ans
        else:
            counter = nums.count(target)
            strt = 0
            for _ in range( counter):
                val =  nums.index(target, strt)
                ans.append(val)
                strt = val +1
        return ans
        

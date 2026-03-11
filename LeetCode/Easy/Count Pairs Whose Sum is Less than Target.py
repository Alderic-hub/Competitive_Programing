class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        length = len(nums)-1
        ans = 0
        for n in range(length):
            counter = 0
            pointer = n + 1
            while pointer <= length:
                val = nums[pointer]+nums[n]
                if val < target:
                    counter += 1
                else:
                    break
                pointer += 1
            ans += counter
        return ans


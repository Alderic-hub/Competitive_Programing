class Solution:
    def twoSum(self, nums, target):
        ans = []
        Nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while start < end:
            value = Nums[start] + Nums[end]
            if value < target:
                start += 1
            elif value > target:
                end -= 1
            else:
                break
        ans.append(nums.index(Nums[start]))
        if Nums[end] == Nums[start]:
            nums.remove(Nums[end])
            val = nums.index(Nums[end]) +1
            ans.append(val)
        else:
            ans.append(nums.index(Nums[end]))
        return ans

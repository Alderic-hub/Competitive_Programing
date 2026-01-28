    def missingNumber(self, nums):
        largest = max(nums)
        Original_val = sum(nums)
        Correct_val = sum(range(1,largest+1))
        ans = Correct_val - Original_val
        if 0 not in nums:
            return 0
        if not ans:
            return largest+1
        return ans

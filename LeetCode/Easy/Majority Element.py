    def majorityElement(self, nums):
        nums.sort()
        length = len(nums)
        half_length = length / 2
        return nums[half_length]

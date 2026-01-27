    def majorityElement(self, nums):
        ans = []
        nums.sort()
        counter = 1
        third = len(nums)//3
        for num in range(len(nums)-1):
            if nums[num] == nums[num+1]:
                counter +=1
            else:
                counter = 1
            if counter > third and nums[num] not in ans:
                ans.append(nums[num])

        if len(nums) < 3:
            return list(set(nums))    
        return ans

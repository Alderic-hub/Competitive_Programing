class Solution(object):
    def numberOfSubarrays(self, nums, k):
        temp_count = 0
        odd_count = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            if nums[right]%2 == 1:
                odd_count += 1
                temp_count = 0
            while odd_count == k:
                if nums[left]%2 == 1:
                    odd_count -= 1
                left += 1
                temp_count+= 1
            ans += temp_count
        return ans

class Solution(object):
    def removeDuplicates(self, nums):
        length = len(nums)-1
        count = 0

        while count < length:
            if nums[count] == nums [count+1]:
                del nums[count]
                length -= 1
                count -=1
            count += 1

        final = len(nums)
        return final
        

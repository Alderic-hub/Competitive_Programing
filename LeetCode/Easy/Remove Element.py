class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        length = len(nums)
        while count < length:
            if nums[count] == val:
                nums.remove(val)
                count-=1
                length-=1
            count +=1
        return len(nums)

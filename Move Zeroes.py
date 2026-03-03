class Solution(object):
    def moveZeroes(self, nums):
        counter = nums.count(0)
        last = len(nums)
        while counter > 0:
            for n  in range(last):
                if nums[n] == 0 :
                    for y in range(n,len(nums)-1):
                        nums[y], nums[y+1] = nums[y+1], nums[y]
                    last -= 1
                    break
            counter -=1

                

        

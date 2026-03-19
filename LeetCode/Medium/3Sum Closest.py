class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        val =None
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums) -1
            while start < end:
                value = target - (nums[i]+nums[start] + nums[end])

                if val == None or abs(value) < val:
                    lis = nums[i] + nums[start] + nums[end]
                    val = abs(value)
         
                if value  > 0:
                    start += 1
                else:
                    end -= 1
        return(lis)
       

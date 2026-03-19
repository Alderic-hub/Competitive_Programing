class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans =[]
        for i in range(len(nums)):
            val = 0 - nums[i]
            start = i+1
            end = len(nums) -1
            while start < end:
                value = abs(val - (nums[start] + nums[end]))
                if value == val:
                    lis = [nums[i], nums[start], nums[end]]
                    if lis not in ans:
                        ans.append(lis)
                    start += 1          
                elif value < val:
                    start += 1
                else:
                    end -= 1
        return(ans)
       

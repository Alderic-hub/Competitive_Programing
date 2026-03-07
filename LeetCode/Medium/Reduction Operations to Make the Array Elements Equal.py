class Solution(object):
    def reductionOperations(self, nums):
        nums = sorted(nums)
        leng = len(nums)
        val = 0
        ans = 0
        for n in range(leng-1):
            val += 1 
            if nums[n] != nums[n+1]:
                ans+=(leng-val)      
        return ans

        


        

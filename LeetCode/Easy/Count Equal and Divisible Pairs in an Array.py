class Solution(object):
    def countPairs(self, nums, k):
        nums_dict = dict(Counter(nums))
        ans_lis = []
        ans = 0
        if len(nums) == len(set(nums)):
            return 0
        for key, value in nums_dict.items():
            lis = []
            if value >= 2:
                for _ in range(value):
                    val = nums.index(key)
                    lis.append(val)
                    nums[val] = -1
                ans_lis.append(lis)
        for items in ans_lis:
            limit = len(items) -1
            for n in range(limit):
                val = items[n]
                for y in range(n + 1, len(items)):
                    if (items[y]*val) % k == 0:
                        ans += 1
           
        return ans


                



                
                

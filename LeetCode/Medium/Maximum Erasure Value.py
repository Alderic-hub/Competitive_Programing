class Solution(object):
    def maximumUniqueSubarray(self, nums):
        unique = []
        ans = 0
        answer = 0
        
        for item in nums:
            if item not in unique:
                ans += item
                unique.append(item)
            else:

                while unique[0] != item:
                    val = unique.pop(0)
                    ans -= val
                val = unique.pop(0)
                ans -= val
                ans += item
                unique.append(item)
            
            if ans > answer:
                answer = ans
        
        return answer

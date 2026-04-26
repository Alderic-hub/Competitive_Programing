class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k 
            if hours <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        return(ans)

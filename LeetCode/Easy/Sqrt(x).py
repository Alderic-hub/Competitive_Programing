class Solution(object):
    def mySqrt(self, x):
        start = 0
        end = x//2
        mid = 0
        if x <= 1:
            return x
        while start <= end:
            mid = (start + end) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                start = mid + 1
            else:
                end = mid - 1
        if mid* mid <= x:
            return mid
        return mid -1
        

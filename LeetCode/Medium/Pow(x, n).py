class Solution(object):
    def myPow(self, x, n):
        val = x
        count = n
        result = 1.0
        
        if count < 0:
            val = 1 / val
            count = -count
        
        while count > 0:
            if count % 2 == 1:
                result *= val
            val *= val
            count //= 2
        
        return result

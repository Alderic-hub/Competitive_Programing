class Solution(object):
    def arrangeCoins(self, n):
        count = 0
        minus = 1
        while n > 0:
            n-=minus
            if n >= 0:
                minus += 1
                count += 1
        return count

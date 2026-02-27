class Solution(object):
    def maxCoins(self, piles):
        piles = sorted(piles)
        ans = 0
        val =len(piles) -2
        while val >= len(piles)//3:
            ans += piles[val]
            val -= 2
        return ans


        

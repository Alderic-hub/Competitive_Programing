class Solution(object):
    def countGoodNumbers(self, n):

        mod = 10**9 + 7
        prime = n // 2
        even = (n + 1) // 2

        ans = (pow(5, even,mod) * pow(4, prime,mod)) 
        return ans


        

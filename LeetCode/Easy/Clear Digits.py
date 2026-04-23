class Solution(object):
    def clearDigits(self, s):
        ans = ''
        alpha = list(string.ascii_lowercase)
        for items in s:
            if items in alpha:
                ans += items
            else:
                ans = ans[:len(ans)-1]
                
        return ans
        

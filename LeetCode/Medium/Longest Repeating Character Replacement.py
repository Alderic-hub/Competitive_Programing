class Solution(object):
    def characterReplacement(self, s, k):
        set_s = set(s)
        length = len(s)
        ans = 0
        for items in set_s:
            start = 0
            count = 0
            for n in range(length):
                if s[n] != items:
                    count += 1
                
                if count > k:
                    if s[start] != items:
                        count -= 1
                    start += 1
                
                if (n - start + 1) > ans:
                    ans = n - start + 1
                    
        return ans


        
        
        

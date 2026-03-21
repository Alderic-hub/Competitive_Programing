class Solution(object):
    def findAnagrams(self, s, p):
        length_p = len(p)
        length_s = len(s)
        start = 0
        end = length_s - length_p
        ans = []
        sorted_s = sorted(p)
        while start <= end:
            arr = sorted(s[start:start+length_p])
            if arr == sorted_s:
                ans.append(start)
            start += 1
        return(ans)
        

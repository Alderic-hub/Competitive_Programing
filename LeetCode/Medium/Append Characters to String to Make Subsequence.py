class Solution(object):
    def appendCharacters(self, s, t):
        val = 0
        length1 = len(s)
        length2 = len(t)
        truth = False
        for n in range(len(s)):
            if val >= length2:
                break
            if s[n] == t[val]:
                val +=1
        
        return len(t[val:])

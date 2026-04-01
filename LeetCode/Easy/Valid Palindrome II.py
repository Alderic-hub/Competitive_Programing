class Solution(object):
    def validPalindrome(self, s):
        start = 0
        end = len(s) -1
        truth = True
        while start < end:
            if s[start] != s [end]:
                truth = False
                val = s[:start] + s[start+1:]
                val2 = s[:end] + s[end+1:]
                break
            start += 1
            end -= 1
        if truth:
            return True
        val1 = val[::-1]
        val22 = val2[::-1]
        if val == val1 or val2 == val22:
            return True
        return False

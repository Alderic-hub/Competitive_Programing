class Solution(object):
    def checkInclusion(self, s1, s2):
        end = len(s1)
        s1 = sorted(s1)
        start = 0
        while end <= len(s2):
            arr = sorted(s2[start:end])
            if arr == s1:
                return True
            start += 1
            end += 1
        return False




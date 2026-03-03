class Solution(object):
    def reverseString(self, s):
        last = len(s) -1
        first = 0
        while first < last:
            s[last], s[first] = s[first], s[last]
            last -= 1
            first += 1

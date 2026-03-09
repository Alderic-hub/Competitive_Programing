class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        length_s = len(s)
        length_g = len(g)
        pointer = 0
        ans = 0
        for n in range(length_g):
            while pointer < length_s:
                if g[n] <= s[pointer]:
                    pointer += 1
                    ans += 1
                    break
                pointer += 1

        return ans
        

class Solution(object):
    def minimumRecolors(self, blocks, k):
        arr = blocks[:k]
        val = arr.count("W")
        start = 0
        ans = val
        for end in range(k,len(blocks)):
            if blocks[start] == 'W':
                val -= 1
            if blocks[end] == "W":
                val += 1
            start += 1
            ans = min(ans, val)
        return ans



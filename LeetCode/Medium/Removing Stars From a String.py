class Solution(object):
    def removeStars(self, s):
        ans = []
        for n in s:
            if n == '*':
                ans.pop()
            else:
                ans.append(n)
        answer = "".join(ans)
        return answer

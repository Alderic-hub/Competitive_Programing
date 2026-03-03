class Solution(object):
    def findRelativeRanks(self, score):
        fal_score = list(score)
        ans = []
        for n in range(len(score)-1,0,-1):
            for y in range(0,n):
                if score[y] > score[y+1]:
                    score[y+1], score[y] = score[y], score[y+1]
        score.reverse()
        for num in fal_score:
            val = score.index(num)
            if val == 0:
                ans.append("Gold Medal")
            elif val == 1:
                ans.append("Silver Medal")
            elif val == 2:
                ans.append("Bronze Medal")
            else:
                val += 1
                ans.append(str(val))
        return ans

        

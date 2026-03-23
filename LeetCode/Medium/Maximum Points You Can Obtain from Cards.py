class Solution(object):
    def maxScore(self, cardPoints, k):
        val_sum = sum(cardPoints)
        discarded = len(cardPoints) - k
        
        if discarded == 0:
            return val_sum
            
        start = 0
        end = discarded
        val = sum(cardPoints[start:end])
        ans = val 
        
        while end < len(cardPoints):
            val -= cardPoints[start]
            val += cardPoints[end]
            start += 1
            end += 1
            
            if val < ans:
                ans = val
        answer = val_sum - ans       
        return answer

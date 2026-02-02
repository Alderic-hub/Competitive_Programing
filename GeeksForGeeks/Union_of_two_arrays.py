class Solution:    
    def findUnion(self, a, b):
        answer = sorted(list(set(a+b)))
        return answer
        

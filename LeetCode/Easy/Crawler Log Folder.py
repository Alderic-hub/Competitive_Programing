class Solution(object):
    def minOperations(self, logs):
        sum = 0
        for items in logs:
            if items == '../':
                if sum > 0:
                    sum -=1
            elif items != './':
                sum +=1
        return sum
                
        

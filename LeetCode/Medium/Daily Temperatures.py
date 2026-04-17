class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0]*len(temperatures)
        values = []
        
        for i,temp in enumerate(temperatures):
            while values and temp > temperatures[values[-1]]:
                prev_index = values.pop()
                ans[prev_index] = i - prev_index
            values.append(i)
            
        return ans
        

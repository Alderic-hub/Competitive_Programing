class Solution(object):
    def judgeSquareSum(self, c):
        lis = [n for n in range(int((c ** 0.5)+1))]
        end = len(lis) - 1
        start = 0
        while start <= end:
            val = lis[start]**2 + lis[end]**2
            print (val)
            if val == c:
                return True
            if val > c:
                end -=1
            elif val < c:
                start +=1
        return False
            


        

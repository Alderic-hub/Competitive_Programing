class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points = sorted(points)
        end = len(points)-1
        ans = 0
        for n in range(end):
            val = abs(points[n][0]-points[n+1][0])
            if val > ans:
                ans = val
        return ans


        

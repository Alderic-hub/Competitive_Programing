class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals)
        ans = []
        n = 0
        if len(intervals) == 1:
            return intervals
        while n < len(intervals)-1:
            lis = intervals[n]
            y = n
            mac = intervals[n][1]
            while y < len(intervals)-1  and  mac >= intervals[y+1][0]:
                lis.extend(intervals[y+1])
                y+=1
                mac = max(mac,intervals[y][1])
            n = y
            small = min(lis)
            big = max(lis)
            ans.append([small,big])
            n+=1
        flat = max([item for sublist in intervals for item in sublist])
        print(flat)
        if intervals[-1][1] == flat and ans[-1][1] != flat:
            
            ans.append(intervals[len(intervals)-1])
        return ans


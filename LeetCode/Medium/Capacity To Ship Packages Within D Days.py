class Solution(object):
    def shipWithinDays(self, weights, days):

        start = max(weights)
        end = sum(weights)
        while start <= end:
            mid = (start + end) // 2
            day = 1
            val = 0
            for n in weights:
                if val + n > mid:
                    day += 1
                    val = n
                else:
                    val += n
                  
            if day <= days:
                end = mid - 1
            else:
                start = mid + 1
        return start

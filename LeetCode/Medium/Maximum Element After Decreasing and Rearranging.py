class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr_sorted = sorted(arr)
        val = 0
        if arr_sorted[0] != 1:
            arr_sorted[0] = 1

        for n in range(1,len(arr)):
            if abs(arr_sorted[n]-arr_sorted[n-1]) > 1:
                arr_sorted[n] = arr_sorted[n-1] + 1 
        
        ans = max(arr_sorted)
        if ans > len(arr):
            return len(arr)
        return ans

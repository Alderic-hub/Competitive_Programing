class Solution(object):
    def duplicateZeros(self, arr):
        length = len(arr)
        n = 0
        while n < length:
            if arr[n]==0:
                arr.insert(n,0)
                arr.pop()
                n+=1
            n+=1
        

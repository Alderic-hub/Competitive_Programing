class Solution: 
    def selectionSort(self, arr):
        length = len(arr)
        for n in range(length):
            for y in range(n+1, length):
                if arr[n] > arr[y]:
                    arr[n], arr[y] = arr[y] , arr[n]
        return arr

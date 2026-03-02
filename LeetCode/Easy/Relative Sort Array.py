class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        ans = []
        left = []
        for n in arr1:
            if n not in arr2:
                left.append(n)
        for n in arr2:
            for y in arr1:
                if n == y:
                    ans.append(n)
        ans += left
        return ans 
                

        

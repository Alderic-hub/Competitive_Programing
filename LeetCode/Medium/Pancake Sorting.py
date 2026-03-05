class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr) -1
        ans = [] 
        decoy = sorted(list(arr))
        k = len(arr)
        for n in range(length):
            if arr != decoy:
                point = arr.index(max(arr[:k]))
                if point == length:
                    k-=1
                elif point == 0:
                    arr[:k]=reversed(arr[:k])
                    ans.append(k)
                    k-=1
                else:
                    point += 1
                    arr[:point] = reversed(arr[:point])
                    ans.append(point)
                    arr[:k]=reversed(arr[:k])
                    ans.append(k)
                    k-=1
            else:
                break
        return ans

            
            
        

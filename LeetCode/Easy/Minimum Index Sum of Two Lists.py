class Solution(object):
    def findRestaurant(self, list1, list2):
        ans = []
        count = 0
        for items in list1:
            if items in list2:
                val = list1.index(items) + list2.index(items)
                if ans == [] or val == count: 
                    ans.append(items)
                    count = val
                elif val < count:
                    ans = [items]
                    count = val
                else:
                    continue
        return ans
            
        

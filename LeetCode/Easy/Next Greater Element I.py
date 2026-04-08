class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        length = len(nums2)
        ans =[]
        for items in nums1:
            place = nums2.index(items)+1 
            added = False
            while place < length:
                val = nums2[place]
                if val > items:
                    added = True
                    ans.append(val)
                    break
                place +=1
            if not added:
               ans.append(-1) 
        return ans

        

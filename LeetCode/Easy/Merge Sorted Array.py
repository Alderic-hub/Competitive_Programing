class Solution(object):
    def merge(self, nums1, m, nums2, n):
        length = len(nums1)
        count = m
        while count < length:
            nums1.pop()
            count +=1
        nums1 += nums2
        nums1.sort()
        
         

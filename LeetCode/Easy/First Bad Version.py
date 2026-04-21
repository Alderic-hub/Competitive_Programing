# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):

        end = n
        start = 1
        count = 0

        while end >= start:
            mid = (end + start)//2
            if not isBadVersion(mid):
                start = mid +1
            else:
                end = mid -1
        if isBadVersion(mid):
            return mid    
        return mid +1

        

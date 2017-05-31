class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if isBadVersion(1):
            return 1
        return self.helper(1,n)
        
    def helper(self, start, stop):
        if isBadVersion(start):
            return start
        
        mid = (start+stop)//2
        if isBadVersion(mid):
            return self.helper(start,mid)
        else:
            return self.helper(mid+1,stop)

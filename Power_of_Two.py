class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n & (n-1) != 0:
            return False
        k = 0
        num = n
        while num!=0:
            k+=1
            num = num >> 1
        if 2**(k-1)==n:
            return True
        return False

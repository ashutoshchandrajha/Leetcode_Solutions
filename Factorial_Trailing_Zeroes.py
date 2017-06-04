class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        f = 5
        while f<=n:
            r += (n/f)
            f *= 5
        return r

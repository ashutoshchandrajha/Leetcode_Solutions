class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x^y
        c = 0
        while xor!=0:
            xor = xor & (xor-1)
            c+=1
        return c

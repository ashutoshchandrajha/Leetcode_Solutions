class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0 or num&(num-1)!=0:
            return False
        n = num
        c = 0
        while n!=0:
            c+=1
            n = n>>1
        if c%2==0:
            return False
        return True

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = 0
        n = num
        while n!=0:
            b+=1
            n = n>>1
        new = 0
        while b>0:
            b-=1
            new = new << 1
            new=new|1
        return num^new

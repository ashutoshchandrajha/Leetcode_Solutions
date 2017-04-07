class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """


        sl = sum([int(k) for k in list(str(num))])
        if len(str(sl))>1:
            return self.addDigits(sl)
        return sl

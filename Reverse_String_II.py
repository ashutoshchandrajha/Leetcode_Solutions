class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        for i in range(0,len(l),2*k):
            new = l[i:i+k]
            l[i:i+k]=new[::-1]
        return ''.join(l)

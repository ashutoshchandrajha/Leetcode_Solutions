class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = 0
        for i in s:
            c = c^ord(i)
        for i in t:
            c = c^ord(i)
        return chr(c)

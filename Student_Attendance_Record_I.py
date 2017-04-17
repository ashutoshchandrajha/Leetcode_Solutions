class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        if "LLL" in s:
            return False
        for i in s:
            if i == "A":
                a+=1
            if a>1:
                return False
        return True

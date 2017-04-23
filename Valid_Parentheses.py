class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = []
        open = ["(","{","["]
        close = [")","}","]"]
        for k in s:
            if k in open:
                l.append(k)
            if k in close:
                if len(l)==0:
                    return False
                if open.index(l[-1])!=close.index(k):
                    return False
                else:
                    l.pop()
        if len(l)==0:
            return True
        else:
            return False

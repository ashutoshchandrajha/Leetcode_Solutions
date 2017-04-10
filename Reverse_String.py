class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        new_str = ''.join(l[i] for i in range(len(l)-1,-1,-1))
        return str(new_str)

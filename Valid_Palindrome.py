class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #i track from front
        #j track from back
        if len(s)==0 or len(s)==1:
            return True
        i = 0
        j = len(s)-1
        while i<=j:
            while i<=j and not s[i].isalnum():
                i+=1
            while i<=j and not s[j].isalnum():
                j-=1
            if not i>j:
                if s[i].lower()!=s[j].lower():
                    return False
            i+=1
            j-=1
        return True

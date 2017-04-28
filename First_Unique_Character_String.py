class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        for i in range(len(s)):
            if len(d[s[i]])==1:
                return i
        return -1

    
#another accepted solution
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0]*256
        for i in s:
            l[ord(i)]+=1
        for i in range(len(s)):
            if l[ord(s[i])]==1:
                return i
        return -1

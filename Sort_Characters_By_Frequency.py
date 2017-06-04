class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        l = []
        for key in sorted(d, key=d.get, reverse=True):
            for k in range(d[key]):
                l.append(key)
        return "".join(l)

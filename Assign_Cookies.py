class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ss = sorted(s)
        gs = sorted(g)
        count = 0
        j = 0
        i = 0
        print(gs)
        print(ss)
        while i<len(gs) and j<len(ss):
            if ss[j]>=gs[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count

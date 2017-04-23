class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        s = "11"
        return self.helper(2,s,n)
        
    def helper(self, j, s, n):
        if j==n:
            return s
        prev=s[0]
        current = ""
        i=0         #track how many chars previously
        for k in s:
            if k==prev:
                i+=1
            else:
                current = current+str(i)+prev
                prev=k
                i=1
        current = current+str(i)+prev
        #print(current)
        return self.helper(j+1,current,n)

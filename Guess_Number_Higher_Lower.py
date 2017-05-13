class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return self.find(1,n)
        
    def find(self, start, stop):
        
        mid = (start+stop)//2
        if guess(mid)==0:
            return mid
        if guess(mid)<0:
            return self.find(start,mid)
        if guess(mid)>0:
            return self.find(mid+1,stop)

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
                
        keys = len(set(candies))
        l = len(candies)//2
        if keys>l:
            return l
        else:
            return keys

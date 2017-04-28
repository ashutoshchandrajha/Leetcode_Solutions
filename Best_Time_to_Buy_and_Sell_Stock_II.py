class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        s = prices[0]
        total = 0
        for i in range(1,len(prices)):
            if prices[i]>s:
                total += prices[i]-s
            s=prices[i]
        return total

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        profit=0
        for i in range(len(prices)):
            buy=min(buy,prices[i])
            profit=max(profit,prices[i]-buy)
        
        return profit
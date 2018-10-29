class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # sold is current sold, current sold = current sold price - current hold - fee
        # hold is current hold, current hold = last sold - current sold price
        sold = 0
        hold = -prices[0]
        for price in prices:
            t = sold
            sold = max(sold, hold + price - fee)
            hold = max(hold, t - price)
        return sold

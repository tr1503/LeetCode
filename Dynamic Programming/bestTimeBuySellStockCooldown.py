# use dp to finish this question, we need two dp arrays to present buy or sell on ith day
# current sell = max(curr sell (last day's sell), current buy + prices[i])
# current buy = max(curr buy (last day's buy), last sell - prices[i])
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        curSell = 0
        prevSell = 0
        buy = -prices[0]
        for i in range(1,len(prices)):
            temp = curSell
            curSell = max(curSell, buy + prices[i])
            if i > 1:
                buy = max(buy, prevSell - prices[i])
            else:
                buy = max(buy, -prices[i])
            prevSell = temp
        return curSell

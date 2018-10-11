#Use dp to finish this question. Set two arrays, one for global profit, another for local profit.
#Because we only have 2 transcation, we need two arrays with length = 3.
#Local profit[i][j] = max(glo[j-1] + max(diff,0), local[j-1] + diff)
#Global profit[i][j] = max(glo[j], local[j])
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        glo = [0] * 3
        local = [0] * 3
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(2,0,-1):
                local[j] = max(glo[j-1] + max(diff,0), local[j] + diff)
                glo[j] = max(local[j],glo[j])
        return glo[2]

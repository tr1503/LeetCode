'''Similar with the third one for k = 2. However, if the number of transaction is more than the length,
we can use the second one, add each profit together and get the answer.'''
class Solution:
    def solveProfit(self, prices):
        res = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
    
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        if k >= len(prices):
            return self.solveProfit(prices)
        glo = [0] * (k + 1)
        local = [0] * (k + 1)
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(k,0,-1):
                local[j] = max(glo[j-1] + max(diff,0), local[j] + diff)
                glo[j] = max(local[j],glo[j])
        return glo[k]

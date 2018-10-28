class Solution:
    def maxGain(self, gain):
        p = [0 for _ in range(len(gain))]
        p[0] = gain[0]
        for i in range(1, len(gain), 1):
            p[i] = max(p[i-1] + gain[i], gain[i])
        
        return max(p)
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) < 2):
            return 0
        gain = []
        for i in range(1, len(prices), 1):
            gain.append(prices[i] - prices[i-1])
        return max(0, self.maxGain(gain))

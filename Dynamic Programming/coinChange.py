'''Use dynamic programming to create a dp array and dp function is 
dp[i] = min(dp[i-coin] + 1, dp[i]) or dp[i + coin] = min(dp[i + coin], dp[i] + 1).'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i+coin],dp[i] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

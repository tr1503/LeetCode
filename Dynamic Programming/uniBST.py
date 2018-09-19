'''Use dynamic programming to create a dp array. The first value dp[0] = 1.
So dp[i] = dp[0]*dp[i-1] + dp[1] * dp[i-2] + dp[2] * dp[i-3] ... + dp[i-1] * dp[0].
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]

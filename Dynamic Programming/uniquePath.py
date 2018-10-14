'''Use dynamtic Programming to create a 1D array to store the paths of each point.'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] += dp[j-1]
        return dp[n-1]

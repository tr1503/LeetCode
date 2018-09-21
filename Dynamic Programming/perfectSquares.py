'''Convert this problem to coin change. It should have less time's way.'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        e = 1
        squares = []
        while e ** 2 <= n:
            squares.append(e**2)
            e += 1
            
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            for square in squares:
                if i + square <= n:
                    dp[i+square] = min(dp[i+square],dp[i] + 1)
        return dp[n]

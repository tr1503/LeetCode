class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0] * 10001
        dp[0] = 1
        now = 0
        for i in range(1,N+1):
            if i <= K:
                now += dp[i-1]
            if i > W:
                now -= dp[i-1-W]
            dp[i] = now/W
        res = 0
        for i in range(K,N+1):
            res += dp[i]
        return res

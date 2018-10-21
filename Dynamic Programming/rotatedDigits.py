class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        dp = [0 for _ in range(N+1)]
        for i in range(N + 1):
            if i < 10:
                if i == 0 or i == 1 or i == 8:
                    dp[i] = 1
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    res += 1
            else:
                a = dp[i // 10]
                b = dp[i % 10]
                if a == 1 and b == 1:
                    dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2
                    res += 1
        return res

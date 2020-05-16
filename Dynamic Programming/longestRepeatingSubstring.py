class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if S[i-1] == S[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        return res

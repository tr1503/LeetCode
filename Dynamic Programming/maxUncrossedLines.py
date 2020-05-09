class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[n][m]

# transfer the dp array's index as F and K and store the max levels they can drop
# Time is O(KlogN), space is O(KN)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        f = 0
        while dp[f][K] < N:
            f += 1
            for j in range(1, K + 1):
                dp[f][j] = dp[f-1][j-1] + dp[f-1][j] + 1
        return f

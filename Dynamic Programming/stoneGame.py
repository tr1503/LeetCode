'''We can pick piles[i] or piles[j].
If Alex picks piles[i], the difference with Lee's pick is piles[i] - piles[i+1][j].
If Alex picks piles[j], the difference with Lee's pick is piles[j] - piles[i][j-1].
State function is dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]).'''
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for j in range(1, len(piles)):
            for i in range(len(piles) - j):
                dp[i][i+j] = max(piles[i] - dp[i+1][i+j], piles[i+j] - dp[i][i+j-1])
        return dp[0][-1] > 0

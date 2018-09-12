'''Use dynamic programming to create a 2d matrix. 
The row is painting this color's min costs. The col is painting different color's min costs.
The state function: dp[i][j] = dp[i][j] + min(dp[i-1][one color except j], dp[i-1][the another except j]).'''
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        dp = [[] for _ in range(len(costs))]
        for i in range(len(dp)):
            dp[i] = [0 for _ in range(3)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1,len(dp)):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        n = len(dp) - 1
        return min(dp[n][0],dp[n][1],dp[n][2])

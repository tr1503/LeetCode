'''Use dynamic programming to store the min cost of climb stairs by one step or two steps. 
The result should be the min number of the last value and the last two value in dp.'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(len(dp)):
            dp[i] = min(cost[i] + dp[i-2], cost[i] + dp[i-1])
        return min(dp[len(dp) - 1], dp[len(dp) - 2])
        

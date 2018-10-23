class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n = len(flights)
        k = len(days[0])
        dp = [-float('inf') for _ in range(n)]
        dp[0] = 0
        for j in range(k):
            t = [-float('inf') for _ in range(n)]
            for i in range(n):
                for p in range(n):
                    if i == p or flights[p][i] != 0:
                        t[i] = max(t[i], dp[p] + days[i][j])
            dp = t
        return max(dp)

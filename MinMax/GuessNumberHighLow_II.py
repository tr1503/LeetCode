class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(start,end,dp):
            if start >= end:
                return 0
            if dp[start][end] > 0:
                #Already have recursion and stored, get the result directly
                return dp[start][end]
            res = float('inf')
            for i in range(start,end+1):
                '''Get minimax value: 
                1) iter each value between 1 to n, get their max value
                2) the max value should be the larger number between current value + smaller interval/larger interval
                3) compare with current min value to get minimax
                '''
                t = i + max(helper(start,i-1,dp), helper(i+1,end,dp))
                res = min(res,t)
            dp[start][end] = res
            return dp[start][end]
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        return helper(0,n,dp)

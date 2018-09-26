'''Use dynamic programming to create a dp matrix.
Check if the value is 1 in the matrix firstly. 
If i = 0, same row last dp value +1.
If j = 0, same col last dp value +1.
Otherwise pick the min value among three values from left, up and left conner.'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m) ]
        res = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    pass
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                res = max(res,dp[i][j] * dp[i][j])
        return res

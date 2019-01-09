# The minimun sum is calculated by the elements from dp's last row and the current element
# Current dp element is calculated from the previous element from original matrix
# Time is O(mn), space is O(mn)
class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        dp = [[0] * (n + 2) for _ in range(m)]
        for i in range(m):
            dp[i][0] = float('inf')
            dp[i][-1] = float('inf')
            for j in range(1,n+1):
                dp[i][j] = A[i][j-1]
        for i in range(1,m):
            for j in range(1,n+1):
                dp[i][j] = A[i][j-1] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        return min(dp[-1])

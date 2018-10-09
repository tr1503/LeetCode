'''Use DFS and DP to solve this question. DP is for memorize the longest path of each vertex'''
class Solution(object): 
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(matrix, x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            #i+1,j | i-1,j | i,j+1 | i,j-1
            dirs = [0,-1,0,1,0]
            dp[x][y] = 1
            for i in range(4):
                nx = x + dirs[i]
                ny = y + dirs[i+1]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or matrix[nx][ny] <= matrix[x][y]:
                    continue
                dp[x][y] = max(dp[x][y], 1 + dfs(matrix,nx,ny))
            return dp[x][y]
        
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(matrix,i,j))
        return ans

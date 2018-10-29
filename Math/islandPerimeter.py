class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 4
                if i > 0 and grid[i-1][j] == 1:
                    res -= 2
                if j > 0 and grid[i][j-1] == 1:
                    res -= 2
        return res

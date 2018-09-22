'''Island has four directions, so we should use dfs to recursive these four directions:
1: i-1, j
2: i+1, j
3: i, j-1
4: i, j+1.
Then use loop to check the value in grid, if one value is 1, go to dfs.
It can prevent the repeated counting.'''
class Solution(object):
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        islands = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid,i,j)
        return islands

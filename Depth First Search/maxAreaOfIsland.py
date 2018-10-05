#Use Flood Fill Algorithm, same solution as number of islands
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        def area(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return 1 + area(i-1,j) + area(i+1,j) + area(i,j-1) + area(i,j+1)
        return max(area(i,j)
                  for i in range(len(grid))
                  for j in range(len(grid[0])))

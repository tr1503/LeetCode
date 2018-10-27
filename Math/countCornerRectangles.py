class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(i+1,m):
                count = 0
                # iter two lines together, get the number of 1
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        count += 1
                # get count - 1 neighbor elements can form how many rectangles: count * (count-1) / 2
                res += count * (count - 1) // 2
        return res

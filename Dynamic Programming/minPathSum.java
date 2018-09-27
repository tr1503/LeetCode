/*
Use dynamic programming to change grid to the dp matrix.
Set the last row and last col to their values adding with right or bottom value,
Because the path is from top or left. And then the other value should be added with
the min value between the right and bottom value. Finally the left conner will be the result.
*/
class Solution {
    public int minPathSum(int[][] grid) {
        for (int i = grid.length - 1; i >= 0; i--) {
            for (int j = grid[0].length - 1; j >= 0; j--) {
                if (i == grid.length - 1 && j != grid[0].length - 1)
                    grid[i][j] = grid[i][j] + grid[i][j+1];
                else if (j == grid[0].length - 1 && i != grid.length - 1)
                    grid[i][j] = grid[i][j] + grid[i+1][j];
                else if (j != grid[0].length - 1 && i != grid.length - 1)
                    grid[i][j] = grid[i][j] + Math.min(grid[i][j+1],grid[i+1][j]);
            }
        }
    return grid[0][0];
    }
}

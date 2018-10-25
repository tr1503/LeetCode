// Create four matrices to represents the number of enemies killed at this position
// from four directions: left to right, right to left, up to bottom, bottom to up
// each position's number of enemies killed should be the sum of these four matrices
class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0)
            return 0;
        int res = 0;
        int m = grid.length;
        int n = grid[0].length;
        int[][] v1 = new int[m][n];
        int[][] v2 = new int[m][n];
        int[][] v3 = new int[m][n];
        int[][] v4 = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int t = (j == 0 || grid[i][j] == 'W') ? 0 : v1[i][j-1];
                v1[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
            for (int j = n - 1; j >= 0; --j) {
                int t = (j == n - 1 || grid[i][j] == 'W') ? 0 : v2[i][j+1];
                v2[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
        }
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                int t = (i == 0 || grid[i][j] == 'W') ? 0 : v3[i-1][j];
                v3[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
            for (int i = m - 1; i >= 0; --i) {
                int t = (i == m - 1 || grid[i][j] == 'W') ? 0 : v4[i+1][j];
                v4[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '0') {
                    res = Math.max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j]);
                }
            }
        }
        return res;
    }
}

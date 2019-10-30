class Solution {
    private int[][] grid;
    private int[][][] memo;
    
    public int cherryPickup(int[][] grid) {
        this.grid = grid;
        int n = grid.length;
        int m = grid[0].length;
        memo = new int[n][m][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(memo[i][j], Integer.MIN_VALUE);
            }
        }
        return Math.max(0, dp(m-1, n-1, m-1));
    }
    
    private int dp(int x1, int y1, int x2) {
        final int y2 = x1 + y1 - x2;
        if (x1 < 0 || y1 < 0 || x2 < 0 || y2 < 0)
            return -1;
        if (grid[y1][x1] < 0 || grid[y2][x2] < 0)
            return -1;
        if (x1 == 0 && y1 == 0)
            return grid[y1][x1];
        if (memo[y1][x1][x2] != Integer.MIN_VALUE)
            return memo[y1][x1][x2];
        memo[y1][x1][x2] = Math.max(Math.max(dp(x1 - 1, y1, x2 - 1), dp(x1, y1 - 1, x2)), Math.max(dp(x1, y1 - 1, x2 - 1), dp(x1 - 1, y1, x2)));
        if (memo[y1][x1][x2] >= 0) {
            memo[y1][x1][x2] += grid[y1][x1];
            if (x1 != x2)
                memo[y1][x1][x2] += grid[y2][x2];
        }
        return memo[y1][x1][x2];
    }
}

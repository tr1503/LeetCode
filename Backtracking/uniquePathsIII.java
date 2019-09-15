// brute force backtracking, time is O(4^(n*m)), space is O(n*m)
class Solution {
    private int res = 0;
    
    public int uniquePathsIII(int[][] grid) {
        int startX = 0, startY = 0, empty = 1;
        int n = grid.length;
        int m = grid[0].length;
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                }
                else if (grid[i][j] == 0) {
                    empty++;
                }
            }
        }
        dfs(grid, startX, startY, empty, visited);
        return res;
    }
    
    private void dfs(int[][] grid, int x, int y, int empty, boolean[][] visited) {
        // condition for end recursion
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] == -1 || visited[x][y])
            return;
        
        // get the end and pass all empties
        if (grid[x][y] == 2 && empty == 0) {
            res++;
            return;
        }
        
        // mark this empty is passed
        visited[x][y] = true;
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (int[] dir : dirs) {
            dfs(grid, x + dir[0], y + dir[1], empty - 1, visited);
        }
        visited[x][y] = false;
    }
}

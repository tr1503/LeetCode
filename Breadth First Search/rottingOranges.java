class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;
        int n = grid.length;
        int m = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) 
                    queue.offer(new int[]{i, j});
                else if (grid[i][j] == 1)
                    fresh++;
            }
        }
        if (fresh == 0)
            return 0;
        int count = 0;
        int[][] dirs = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        while (!queue.isEmpty()) {
            count++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] p = queue.poll();
                for (int[] d : dirs) {
                    int x = p[0] + d[0];
                    int y = p[1] + d[1];
                    if (x < 0 || y < 0 || x >= n || y >= m || grid[x][y] == 0 || grid[x][y] == 2)
                        continue;
                    grid[x][y] = 2;
                    queue.offer(new int[]{x, y});
                    fresh--;
                }
            }
        }
        return fresh == 0 ? count-1 : -1;
    }
}

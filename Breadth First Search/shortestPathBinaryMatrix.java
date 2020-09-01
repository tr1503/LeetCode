class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0},{1,-1},{-1,1},{-1,-1},{1,1}};
        if (grid[0][0] == 1 || grid[m-1][n-1] == 1) {
            return -1;
        }
        
        boolean[][] visited = new boolean[m][n];
        visited[0][0] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0,0});
        int res = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                if (curr[0] == m - 1 && curr[1] == n - 1)
                    return res + 1;
                for (int j = 0; j < 8; j++) {
                    int nx = dirs[j][0] + curr[0];
                    int ny = dirs[j][1] + curr[1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && grid[nx][ny] == 0) {
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            res++;
        }
        return -1;
    }
}
